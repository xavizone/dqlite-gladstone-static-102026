# Bonus B1 - Budgets and resource monitors
# Co-authored with CoCo
import streamlit as st

import sample_data as D
from ui import capability, explanations, footer, header, result_label, sql_steps, step, table, what_why

P = "bonus_b1"
header(P)
capability("Cost visibility and guardrails per operator: Dynamic Table refresh cost, cost-attribution tags on the "
           "operator schema, a custom **budget** with an 80% email alert, and **resource monitors** on warehouses.",
           "Bonus B1 (after the session)", "`sql/bonus/B1_setup.sql` runs without error")
what_why(P)

st.divider()
step(P, 0)
st.markdown("**Demo results: refresh work per REPORTING Dynamic Table** (`DYNAMIC_TABLE_REFRESH_HISTORY`)")
result_label()
table(D.B1_DT_COST)
st.caption("Serverless DMF credits come from `ACCOUNT_USAGE.DATA_QUALITY_MONITORING_USAGE_HISTORY`, which lags up to about 3 hours.")

st.divider()
step(P, 1)
st.markdown("**Demo results: tags on `RIVERSIDE_NIELS`** - every table and Dynamic Table inside inherits them")
result_label()
table(D.B1_TAGS)

st.divider()
step(P, 2)
st.markdown("**Demo results: the operator budget**")
result_label()
m1, m2, m3 = st.columns(3)
m1.metric("Monthly spending limit", f"{D.B1_LIMIT[0]['GET_SPENDING_LIMIT']} credits")
m2.metric("Email alert at", f"{D.B1_THRESHOLD[0]['GET_NOTIFICATION_THRESHOLD']}% projected")
m3.metric("Linked resources", len(D.B1_LINKED))
table(D.B1_LINKED)
st.caption("Spending history fills in after the budget's background refresh, which can take hours.")

st.divider()
step(P, 3)
st.markdown("**Demo results: resource monitors and the lab warehouse**")
result_label()
table(D.B1_MONITORS)
table(D.B1_WH)

explanations(P)
sql_steps(P)
footer(P)
