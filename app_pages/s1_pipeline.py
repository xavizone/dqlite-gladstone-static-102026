# Session 1 - The complaint
# Co-authored with CoCo
import streamlit as st

import story

import sample_data as D
from ui import (capability, checkpoints, explanations, footer, header, prompt, result_label, snowsight,
                sql_steps, table, tech, what_why)

P = "session_01"
header(P)
story.chapter(1)
st.info(""":material/support_agent: **Riverside Leisure, on the phone to Customer Success:**
*"Nova says we have more active members than our front desk can count, and today's revenue looks far too low."*""")
capability("Map one operator's Nova pipeline end to end - Bronze tables, the merge task, REPORTING Dynamic Tables "
           "and the semantic view - from live metadata, by asking CoCo.",
           "Session 1 (5 min)", "`SHOW DYNAMIC TABLES` and `DESCRIBE SEMANTIC VIEW` in your schema")
what_why(P)

st.divider()
prompt(P, 0)
snowsight(P, 0)

st.subheader("Demo results: what CoCo finds")
result_label()
c1, c2 = st.columns([3, 2])
with c1:
    st.markdown("**Objects in `RIVERSIDE_NIELS`**")
    table(D.S1_OBJECTS)
with c2:
    st.markdown("**Rows per Bronze table**")
    table(D.S1_COUNTS)
st.markdown("**REPORTING Dynamic Tables** - all INCREMENTAL, 1-minute target lag")
table(D.S1_DTS)
st.markdown("**Simulated Bifrost merge task**")
table(D.S1_TASKS)
st.graphviz_chart("""
digraph { rankdir=LR; node [shape=box, style="rounded,filled", fillcolor="#F0F4F8", color="#29B5E8", fontname="Helvetica"];
  task [label="TSK_BIFROST_MERGE\\n1 min"]; b [label="Bronze\\nMEMBERS__ / SHARED__ / SYSTEM__"];
  s [label="REPORTING__ACTIVE_MEMBERS\\nREPORTING__DAILY_REVENUE\\nREPORTING__CLASS_UTILISATION"];
  g [label="SV_RIVERSIDE_KPIS\\n+ vq_active_members"]; n [label="Nova answer"];
  task -> b -> s -> g -> n; }""", width="stretch")

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.subheader("Demo results: the clean baseline")
result_label()
two = D.S1_TWO_ACTIVE[0]
m1, m2, m3 = st.columns(3)
m1.metric("Active members (source status)", f"{two['ACTIVE_MEMBERS']:,}")
m2.metric("Active members (paid in 35 days, verified query)", f"{two['PAID_MEMBERS_35D']:,}")
m3.metric("Gap on clean data", f"{(two['ACTIVE_MEMBERS'] - two['PAID_MEMBERS_35D']) / two['ACTIVE_MEMBERS']:.1%}")
st.markdown("**Net revenue, last 3 days** (semantic view `rev.net_revenue`)")
table(D.S1_REVENUE)

checkpoints(P)
story.turn(1)
explanations(P)
tech(P)
sql_steps(P)
footer(P)
