# Session 2 - Put guards on it
# Co-authored with CoCo
import json

import streamlit as st

import story

import sample_data as D
from snippets import PAGES
from ui import (capability, checkpoints, expectations_table, explanations, footer, header, prompt, result_label,
                snowsight, sql_steps, table, tech, what_why)

P = "session_02"
header(P)
story.chapter(2)
capability("Data metric functions (system and custom) with **expectations** - rules that must always hold - plus "
           "email notifications and an **alert** that logs every failure to `DQ_INCIDENTS`.",
           "Session 2 (8 min)", "`SHOW DATA METRIC FUNCTIONS IN SCHEMA SNOWFLAKE.CORE`; `EXECUTE ALERT` granted")
what_why(P)

st.divider()
prompt(P, 0)
snowsight(P, 0)
st.subheader("Demo results: the guards")
result_label()
rows = [{"TABLE": r["REF_ENTITY_NAME"], "METRIC": r["METRIC_NAME"],
         "COLUMNS": ", ".join(a["name"] for a in json.loads(r["REF_ARGUMENTS"])) or "(table)",
         "STATUS": r["SCHEDULE_STATUS"]} for r in D.S2_ATTACHED]
st.markdown("**Attached checks** (`DATA_METRIC_FUNCTION_REFERENCES`, every 5 minutes)")
table(rows)
clean = D.S2_CLEAN_MEMBERS__MEMBER + D.S2_CLEAN_SYSTEM__PAYMENT + D.S2_CLEAN_SYSTEM__ATTENDANCE
c1, c2 = st.columns([1, 3])
c1.metric("Expectations evaluated now", len(clean))
c1.metric("Violated", sum(1 for r in clean if r["EXPECTATION_VIOLATED"]))
with c2:
    expectations_table(clean)
st.caption("`SYSTEM$EVALUATE_DATA_QUALITY_EXPECTATIONS` runs single-table checks on demand. "
           "`reporting_within_5min` compares two tables and runs on its schedule.")

st.divider()
prompt(P, 1)
snowsight(P, 1)
st.subheader("Demo results: the incident alert is armed")
result_label()
c1, c2 = st.columns([3, 1])
with c1:
    table(D.S2_ALERTS)
c2.metric("Rows in DQ_INCIDENTS", D.S2_INCIDENTS_EMPTY[0]["INCIDENTS"], help="Empty until a check fails")

checkpoints(P)
story.turn(2)
concepts = PAGES[P].get("concepts", [])
if concepts:
    st.markdown("##### :material/lightbulb: Key concepts")
    for c in concepts:
        with st.expander(f"**{c['term']}**"):
            st.markdown(c["definition"])
explanations(P)
tech(P)
sql_steps(P)
footer(P)
