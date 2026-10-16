# Session 4 - Operate it
# Co-authored with CoCo
import streamlit as st

import story

import sample_data as D
from snippets import PAGES
from ui import (capability, checkpoints, explanations, footer, header, prompt, result_label, snowsight,
                sql_steps, table, tech, what_why)

P = "session_04"
header(P)
story.chapter(4)
story.ticket("s4")
capability("One health view per operator (`V_DQ_HEALTH`) over the expectation results and the incident log, a "
           "business-rule fault caught by a custom DMF, and a breaker that closes by itself after the fix.",
           "Session 4 (8 min)", "`CREATE VIEW` over `SNOWFLAKE.LOCAL` in your schema")
what_why(P)

st.divider()
st.code("CALL GLADSTONE_DQ_LITE.ADMIN.INJECT('ALL', 4);   -- minute 23: cancelled members re-sent as ACTIVE", language="sql")
prompt(P, 0)
snowsight(P, 0)
st.subheader("Demo results: what Customer Success sees")
result_label()


def health(rows):
    st.dataframe(rows, hide_index=True, width="stretch",
                 column_order=["STATUS", "TABLE_NAME", "EXPECTATION_NAME", "VALUE", "LAST_CHECKED", "INCIDENTS"],
                 column_config={"STATUS": st.column_config.TextColumn("Status")})


state = st.segmented_control("Show", ["Faults present", "After the fix"], default="Faults present", key="h_state") or "Faults present"
if state == "Faults present":
    bad = [r for r in D.S4_HEALTH_FAIL if r["STATUS"] == "FAILING"]
    st.error(f"**{len(bad)} of {len(D.S4_HEALTH_FAIL)} checks FAILING** - don't trust Riverside's Nova numbers right now.",
             icon=":material/error:")
    health(D.S4_HEALTH_FAIL)
    st.markdown("**Incident log** (`DQ_INCIDENTS`)")
    table(D.S4_INCIDENTS)
else:
    ok = [r for r in D.S4_HEALTH_OK2 if r["STATUS"] == "OK"]
    st.success(f"**{len(ok)} of {len(D.S4_HEALTH_OK2)} checks OK** - Riverside's numbers are back.", icon=":material/check_circle:")
    health(D.S4_HEALTH_OK2)

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.subheader("Demo results: fix, recover, compare")
result_label()
c1, c2 = st.columns([2, 3])
with c1:
    st.markdown("**Rows the source team fixed**")
    table(D.S4_FIX)
with c2:
    closed = [r for r in D.S4_BREAKER_CLOSED if r["RETURN_VALUE"]]
    st.success(f"**{closed[0]['RETURN_VALUE']}**", icon=":material/check_circle:")
    table(closed)
st.markdown("REPORTING running again:")
table(D.S4_DTS_CLOSED)
before, after = D.S1_TWO_ACTIVE[0], D.S4_TWO_ACTIVE[0]
m1, m2 = st.columns(2)
m1.metric("Active members (status) after the fix", f"{after['ACTIVE_MEMBERS']:,}",
          delta=f"{after['ACTIVE_MEMBERS'] - before['ACTIVE_MEMBERS']:+,} vs clean baseline", delta_color="off")
m2.metric("Active members (paid in 35 days)", f"{after['PAID_MEMBERS_35D']:,}",
          delta=f"{after['PAID_MEMBERS_35D'] - before['PAID_MEMBERS_35D']:+,} vs clean baseline", delta_color="off")
with st.expander(":material/info: The first health check after the fix"):
    st.caption("While the breaker was OPEN, REPORTING fell behind Bronze on purpose. The first check after it closes "
               "flags `reporting_within_5min` once; the next run passes.")
    health(D.S4_HEALTH_OK)

checkpoints(P)
story.turn(4)
story.epilogue()
built = PAGES[P].get("built", [])
if built:
    st.markdown("##### :material/check_circle: What you built")
    for b in built:
        st.markdown(f"- :green-badge[Done] {b}")
explanations(P)
tech(P)
sql_steps(P)
footer(P)
