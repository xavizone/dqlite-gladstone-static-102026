# Bonus B3 - DevOps with DCM Projects
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

import sample_data as D
from ui import capability, explanations, footer, header, result_label, step, what_why

P = "bonus_b3"
DCM = Path(__file__).parent.parent / "sql" / "bonus" / "dcm_project"
header(P)
capability("One operator's pipeline and its data quality checks as code: a DCM project with a target per operator, "
           "`plan` before `deploy`, and `snow dcm test` as a CI gate.",
           "Bonus B3 (after the session)", "`snow dcm create` in a pre-created `RIVERSIDE_<NAME>_DCM` schema (Snowflake CLI 3.17+)")
what_why(P)

st.divider()
step(P, 0)
st.markdown("**Demo results: `snow dcm create`**")
result_label()
st.code(D.B3_CREATE_OUT, language="text")

st.divider()
step(P, 1)
st.markdown("**Demo results: plan, then deploy**")
result_label()
c1, c2 = st.columns(2)
with c1:
    st.markdown("`snow dcm plan --save-output`")
    st.code(D.B3_PLAN_OUT[-900:], language="text")
with c2:
    st.markdown("`snow dcm deploy --alias first-deploy`")
    st.code(D.B3_DEPLOY_OUT[-900:], language="text")

st.divider()
step(P, 2)
st.markdown("**Demo results: test, break, test again**")
result_label()
first, second = st.columns(2)
with first:
    st.markdown(":green-badge[exit 0] Clean data")
    st.code(D.B3_TEST_OUT, language="text")
with second:
    st.markdown(f":red-badge[exit {D.B3_TEST_FAIL_EXIT}] After inserting a duplicate `member_id`")
    st.code(D.B3_TEST_FAIL_OUT, language="text")
st.caption("A non-zero exit code fails the CI step - bad data or a broken definition never reaches the next stage.")

st.divider()
step(P, 3)
explanations(P)

st.markdown("##### :material/folder_open: Answer key project (`sql/bonus/dcm_project`)")
for f in ["manifest.yml", "sources/definitions/bronze.sql", "sources/definitions/reporting.sql",
          "sources/definitions/expectations.sql", ".github/workflows/operator-pipeline-dcm.yml"]:
    with st.expander(f":material/description: `{f}`"):
        st.code((DCM / f).read_text(), language="yaml" if f.endswith(".yml") else "sql")
st.code("""cd operator_pipeline
snow dcm create  --target NIELS -c <conn>
snow dcm plan    --target NIELS -c <conn> --save-output    # read out/plan/plan_result.json
snow dcm deploy  --target NIELS -c <conn> --alias first-deploy
snow dcm test    --target NIELS -c <conn>""", language="bash")
footer(P)
