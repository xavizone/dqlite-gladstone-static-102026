# Session 3 - Catch, explain, contain
# Co-authored with CoCo
import streamlit as st

import story

import sample_data as D
from ui import (capability, checkpoints, explanations, footer, header, prompt, result_label, snowsight,
                sql_steps, table, tech, what_why)

P = "session_03"
header(P)
story.chapter(3)
capability("Catch faults as they land (expectations + the incident alert), explain them with failing rows and the "
           "merge batch, and **contain** them with a circuit breaker that freezes REPORTING.",
           "Session 3 (9 min)", "`SNOWFLAKE.LOCAL.DATA_QUALITY_MONITORING_EXPECTATION_STATUS` returns rows for your schema")
what_why(P)

st.divider()
st.subheader("Minutes 13-18: the facilitator breaks Riverside's pipeline")
st.code("""CALL GLADSTONE_DQ_LITE.ADMIN.INJECT('ALL', 1);   -- Bifrost replay
CALL GLADSTONE_DQ_LITE.ADMIN.INJECT('ALL', 2);   -- refund sign flip
CALL GLADSTONE_DQ_LITE.ADMIN.INJECT('ALL', 3);   -- merge task stalled""", language="sql")
if st.button("Inject faults 1-3 (replay the captured run)", type="primary", icon=":material/bolt:"):
    st.session_state["faults_on"] = True


def faulted():
    story.ticket("s3")
    result_label("Captured from a real run, about 5 minutes after injection")
    table(D.F_FAULTS, cols=["FAULT_NO", "FAULT_CODE", "DESCRIPTION", "CAUGHT_BY"])
    st.markdown("#### :material/notifications_active: Caught: `DQ_INCIDENTS`, written by the alert")
    st.caption("Nobody ran a query: the scheduled checks failed and the alert logged them within a minute.")
    table(D.S3_INCIDENTS)

    st.divider()
    prompt(P, 0)
    snowsight(P, 0)
    st.subheader("Demo results: what CoCo finds")
    before, now = D.S1_TWO_ACTIVE[0], D.S3_TWO_ACTIVE[0]
    rev_before = {r["PAYMENT_DATE"]: float(r["NET_REVENUE"]) for r in D.S1_REVENUE}
    rev_now = {r["PAYMENT_DATE"]: float(r["NET_REVENUE_BRONZE"]) for r in D.S3_REVENUE_BRONZE}
    today = max(rev_now)
    m1, m2, m3 = st.columns(3)
    m1.metric("Active members (status)", f"{now['ACTIVE_MEMBERS']:,}", delta=f"{now['ACTIVE_MEMBERS'] - before['ACTIVE_MEMBERS']:+,} vs clean")
    m2.metric("Today's net revenue in Bronze", f"£{rev_now[today]:,.0f}",
              delta=f"£{rev_now[today] - rev_before.get(today, rev_now[today]):+,.0f} vs clean")
    m3.metric("Failing expectations", len(D.S3_FAILING))
    tabs = st.tabs(["Failing checks", "Duplicate rows", "Merge batches", "Negative payments", "Merge task"])
    with tabs[0]:
        table(D.S3_FAILING, cols=["TABLE_NAME", "EXPECTATION_NAME", "METRIC_NAME", "VALUE", "MEASUREMENT_TIME"])
    with tabs[1]:
        st.caption("`SYSTEM$DATA_METRIC_SCAN` on `DUPLICATE_COUNT(member_id)` - each member twice, the copy from `B-REPLAY-01`")
        table(D.S3_SCAN)
    with tabs[2]:
        st.caption("`_SYNC_META__MERGE_BATCH`: the same batch recorded twice")
        table(D.S3_BATCHES)
    with tabs[3]:
        table(D.S3_NEGATIVE)
    with tabs[4]:
        st.caption("Suspended: no new payments, so FRESHNESS passes 180 seconds")
        table(D.S3_TASK)

    st.divider()
    prompt(P, 1)
    snowsight(P, 1)
    st.subheader("Demo results: contained")
    st.error(f"**{D.S3_BREAKER_OPEN[0]['RETURN_VALUE']}**", icon=":material/block:")
    table(D.S3_BREAKER_OPEN)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("REPORTING paused - no further refreshes:")
        table(D.S3_DTS_OPEN)
    with c2:
        st.markdown("What Nova shows: the first bad batch had already refreshed (checks every 5 min, REPORTING every 1 min - see *Nova already shows the bad revenue - why?* below):")
        table(D.S3_REVENUE_NOVA)


if st.session_state.get("faults_on"):
    faulted()
else:
    st.caption("Press the button to see what the guards caught.")

checkpoints(P)
story.turn(3)
explanations(P)
tech(P)
sql_steps(P)
footer(P)
