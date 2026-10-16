# Overview - the complaint, the pipeline, the agenda
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

from ui import footer

_STATIC = Path(__file__).parent.parent / "static"

with st.container(horizontal=True, vertical_alignment="center", gap="large"):
    st.image(str(_STATIC / "gladstone_logo.jpg"), width=110)
    st.image(str(_STATIC / "snowflake_full_logo.png"), width=180)
st.title("Catch it before the operator does - data quality lab (Lite)")

st.info("""**Capability:** Native, proactive data quality for one operator's Nova pipeline - data metric functions,
expectations, notifications, alerts, a circuit breaker and a health view - driven by prompts in **CoCo Desktop or CLI**.

**This app:** a read-only preview. Every result shown was captured from a real run of the lab; nothing connects to Snowflake.""",
        icon=":material/info:")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Core lab", "30 min", help="Sessions 1-4")
c2.metric("Prompts", "8 core", help="Plus stretch and bonus prompts")
c3.metric("Faults", "4", help="Injected live, the same for everyone")
c4.metric("Bonus labs", "3", help="Budgets, governance + GDPR, DCM DevOps")

st.markdown("""
### Why this matters
**Riverside Leisure** (a fictional operator with three sites in Oxfordshire) rings Customer Success:

> *"Nova says we have more active members than our front desk can count, and today's revenue looks far too low."*

The answer came from Nova's semantic view, reading REPORTING Dynamic Tables, built from Bronze tables that Bifrost
merges in from Riverside's Azure SQL. Today Gladstone finds out **when the operator rings**.

### What we'll demonstrate
1. Reproduce the complaint and map the pipeline (Session 1)
2. Put guards on it: expectations, an email, and an incident-logging alert (Session 2)
3. Catch live faults, explain them, and contain them with a circuit breaker (Session 3)
4. Operate it: one health view, a business-rule fault, fix and recover (Session 4)

### Outcome
The next bad Bifrost batch becomes an incident row and an email within minutes, the REPORTING refresh is paused, and Customer Success can tell the operator *"we know, it's fixed"* before they call.
""")

st.markdown("### Riverside's pipeline")
st.graphviz_chart("""
digraph {
  rankdir=LR; node [shape=box, style="rounded,filled", fillcolor="#F0F4F8", color="#29B5E8", fontname="Helvetica"];
  src [label="Riverside Azure SQL\\n(source)"]; task [label="TSK_BIFROST_MERGE\\n(simulated Bifrost, 1 min)"];
  bronze [label="Bronze\\nMEMBERS__* / SHARED__* / SYSTEM__*"]; dt [label="Silver REPORTING\\nDynamic Tables"];
  sv [label="Gold\\nSV_RIVERSIDE_KPIS"]; nova [label="Nova answer"];
  dq [label="Guards: DMFs + expectations", fillcolor="#E3F5FC"];
  inc [label="Alert -> DQ_INCIDENTS\\n+ email", fillcolor="#E3F5FC"];
  cb [label="Circuit breaker", fillcolor="#E3F5FC"];
  src -> task -> bronze -> dt -> sv -> nova;
  dq -> bronze [style=dashed, arrowhead=none]; dq -> dt [style=dashed, arrowhead=none];
  dq -> inc [style=dashed]; dq -> cb [style=dashed]; cb -> dt [style=dashed, label="suspend"];
}""", width="stretch")

st.markdown("### Agenda")
st.markdown("""
| Time | Section | You do (in CoCo) | Snowflake capability |
|---|---|---|---|
| 0-5 | **1. The complaint** | Map the pipeline; reproduce the two numbers | Lineage, Dynamic Tables, Tasks, semantic view |
| 5-13 | **2. Put guards on it** | Expectations; email + incident alert | DMFs, expectations, notifications, alerts |
| 13-22 | **3. Catch, explain, contain** | "What broke, why, stop it reaching Nova" | DQ results, failing rows, task history, circuit breaker |
| 22-30 | **4. Operate it** | Health view, fault 4, fix and recover | Views, incident log, `SYSTEM$SET_RETURN_VALUE` |
""")

st.markdown("### The faults (captured run)")
st.markdown("""
| # | What happened (in Nova terms) | What the operator sees | Caught by |
|---|---|---|---|
| 1 | Bifrost applied the same merge batch twice | +150 active members | `DUPLICATE_COUNT` = 150 |
| 2 | Refunds arrived as negative payments | Today's revenue down £10,000 | `NEGATIVE_COUNT` = 40 |
| 3 | The sync task stopped | Nothing new arriving | `FRESHNESS` over 180 s |
| 4 | Cancelled members re-sent as ACTIVE | Two "active members" answers drift apart | `ACTIVE_BUT_LEFT` = 292 |
| 5 (stretch) | A day of bookings went missing | Utilisation drops | Anomaly detection on `ROW_COUNT` |
""")

st.markdown("### From reactive to proactive")
st.markdown("""
| Today | After this lab | Session |
|---|---|---|
| The operator notices wrong numbers | A check fails within minutes of the bad batch | 2-3 |
| CS opens a ticket and waits for engineering | An incident row and an email already say which check, table and batch | 2-3 |
| Wrong numbers keep flowing into Nova | A circuit breaker pauses REPORTING until Bronze is clean | 3 |
| No single view of pipeline health | `V_DQ_HEALTH`: every check, OK/FAILING, incidents | 4 |
""")
footer("home")
