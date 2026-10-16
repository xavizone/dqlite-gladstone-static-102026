# Bonus B2 - Data governance and GDPR
# Co-authored with CoCo
import json
from pathlib import Path

import pandas as pd
import streamlit as st

import sample_data as D
from ui import capability, explanations, footer, header, result_label, step, table

P = "bonus_b2"
header(P)
capability("Classification, **tag-based masking**, **row access per site**, and three GDPR workflows - record of "
           "processing, subject access request, and an erasure proved by a data quality check.",
           "Bonus B2 (after the session)", "`SYSTEM$CLASSIFY` and `sql/bonus/B2_setup.sql` succeed (Enterprise Edition)")
st.warning("Synthetic data only. This is a technical pattern, not legal advice - confirm decisions with Gladstone's DPO.",
           icon=":material/gavel:")

tab_a, tab_b = st.tabs([":material/policy: Part A - governance", ":material/gavel: Part B - GDPR exercise"])

with tab_a:
    step(P, 0)
    st.markdown("**Demo results: `SYSTEM$CLASSIFY` on `MEMBERS__MEMBER`** (suggestions only - nothing tagged yet)")
    result_label()
    cls = D.B2_CLASSIFY_JSON["classification_result"]
    rows = [{"COLUMN": c, "SEMANTIC_CATEGORY": v["recommendation"]["semantic_category"],
             "PRIVACY_CATEGORY": v["recommendation"]["privacy_category"], "CONFIDENCE": v["recommendation"]["confidence"]}
            for c, v in cls.items() if v.get("recommendation")]
    table(rows)
    st.caption("`HEALTH_NOTES` is not a built-in category - that's why the lab tags it by hand as special-category data.")

    st.divider()
    step(P, 1)
    st.markdown("**Demo results: the same query, two roles**")
    result_label()
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("As pipeline role `DQ_LITE_ATTENDEE` - **masked**")
        table(D.B2_MASKED_OWNER)
    with c2:
        st.markdown("As privacy role `DQ_LITE_PII_READER` - **clear**")
        table(D.B2_CLEAR_READER)
    st.caption("Email keeps its domain, date of birth keeps the year only, everything else is replaced. One policy on the tag covers every tagged column.")

    st.divider()
    step(P, 2)
    st.markdown("**Demo results: row access by site**")
    result_label()
    c1, c2, c3 = st.columns([1, 1, 2])
    with c1:
        st.markdown("Pipeline role `DQ_LITE_ATTENDEE`")
        table(D.B2_SITE_OWNER)
    with c2:
        st.markdown("Site role `DQ_LITE_SITE_VIEWER`")
        table(D.B2_SITE_VIEWER)
    with c3:
        st.markdown("What the site role sees (S01 only, masked)")
        table(D.B2_VIEWER_ROWS)

    st.divider()
    step(P, 3)
    st.markdown("**Demo results: what Nova's semantic view reads**")
    result_label()
    sv = pd.DataFrame(D.B2_SV_DESCRIBE)
    base = sv[(sv["object_kind"] == "TABLE") & (sv["property"] == "BASE_TABLE_NAME")][["object_name", "property_value"]]
    table(base.rename(columns={"object_name": "ALIAS", "property_value": "BASE_TABLE"}).to_dict("records"))
    st.caption("REPORTING aggregates and memberships only - no member name, contact or health columns reach Nova.")

with tab_b:
    st.markdown("##### :material/rule: Things to consider first")
    st.markdown("""
| Topic | Question for Gladstone and each operator |
|---|---|
| Roles | Is Gladstone the processor and the operator the controller for member data? Who receives SARs? |
| Lawful basis | Contract (membership), legal obligation (payments), consent (marketing), explicit consent (health notes)? |
| Special category | PAR-Q / health notes need an Article 9 condition. Should they reach Snowflake or Nova at all? |
| Retention | How long after a membership ends? Payments usually longer (tax). |
| Copies | Time Travel, Fail-safe, clones, dev/test copies, Nova caches, exported files. |
| Residency | UK South storage; Cortex cross-region inference setting (`CORTEX_ENABLED_CROSS_REGION`). |
| Timelines | SAR within one month; breach notification to the ICO within 72 hours where required. |
""")
    st.markdown("##### :material/alt_route: Approaches to erasure")
    st.markdown("""
| Approach | When | Trade-off |
|---|---|---|
| Hard delete | Bookings, attendance, marketing data | Simple; breaks history and aggregates |
| Pseudonymise | Payments you must keep for tax | Keeps finance intact; still personal data if the key/salt can re-identify |
| Crypto-shredding | Per-member keys outside Snowflake | Strong, but complex to run at scale |
| Retention policy | Scheduled expiry of old members | Automates storage limitation; needs agreed periods |
""")

    st.divider()
    step(P, 4)
    st.markdown("**Demo results: record of processing** (column tags in `GOVERNANCE`)")
    result_label()
    tags = pd.DataFrame(D.B2_GDPR_TAGS).pivot_table(index="COLUMN_NAME", columns="TAG_NAME", values="TAG_VALUE", aggfunc="first").reset_index()
    table(tags.fillna("").to_dict("records"))

    st.divider()
    step(P, 5)
    st.markdown("**Demo results: SAR export for M-01043** (run with `DQ_LITE_PII_READER` as a secondary role)")
    result_label()
    sar = D.B2_SAR_JSON
    st.metric("Tables with rows for this member", len(sar["data"]))
    st.json(sar, expanded=1)
    st.download_button("Download SAR JSON", data=json.dumps(sar, indent=2), file_name="SAR_M-01043.json",
                       mime="application/json", icon=":material/download:")

    st.divider()
    step(P, 6)
    st.markdown("**Demo results: erasure of M-01042**")
    result_label()
    e = D.B2_ERASE_JSON
    m = st.columns(4)
    for col, (k, label) in zip(m, [("member_rows", "Member rows pseudonymised"), ("payments_pseudonymised", "Payments kept, pseudonymised"),
                                   ("bookings_deleted", "Bookings deleted"), ("attendance_deleted", "Check-ins deleted")]):
        col.metric(label, e[k])
    table(D.B2_REQUESTS)

    st.divider()
    step(P, 7)
    st.markdown("**Demo results: `erasure_complete` expectation**")
    result_label()
    er = [r for r in D.B2_ERASURE_EVAL if r["METRIC_NAME"] == "ERASED_MEMBERS_STILL_PRESENT"]
    table(er)

    st.divider()
    step(P, 8)
    st.markdown("**Demo results: copies that survive**")
    result_label()
    m1, m2, m3 = st.columns(3)
    m1.metric("Rows for M-01042 in Time Travel (2 min ago)", D.B2_TIMETRAVEL[0]["STILL_IN_TIME_TRAVEL"])
    m2.metric("MEMBERS__MEMBER retention (days)", D.B2_RETENTION[0]["retention_time"])
    m3.metric("CORTEX_ENABLED_CROSS_REGION", D.B2_CROSS_REGION[0]["value"], help="Value on the demo account - check yours")
    st.caption("The cross-region value above is the demo account's. Gladstone's admin should check `GLADSTONESOFTWARE` and agree the setting with the DPO.")
    explanations(P)
    with st.expander(":material/description: Full B2 answer key"):
        st.code((Path(__file__).parent.parent / "sql" / "bonus" / "B2_answer_key.sql").read_text(), language="sql", line_numbers=True)

footer(P)
