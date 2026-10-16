# Gladstone MRM | Data quality lab (Lite) - static backup for streamlit.io
# Co-authored with CoCo
# No Snowflake connection required - every result shown was captured from a real run of the lab
from pathlib import Path

import streamlit as st

_DIR = Path(__file__).parent

st.set_page_config(page_title="Gladstone MRM | Data quality lab Lite (read-only)", page_icon=":material/fact_check:", layout="wide")
st.logo(str(_DIR / "static" / "snowflake_full_logo.png"), icon_image=str(_DIR / "static" / "snowflake_logo.png"))

page = st.navigation({
    "": [
        st.Page("app_pages/overview.py", title="Overview", icon=":material/home:"),
        st.Page("app_pages/before_you_start.py", title="Before you start", icon=":material/event_available:"),
        st.Page("app_pages/install_coco.py", title="Install CoCo Desktop and CLI", icon=":material/download:"),
        st.Page("app_pages/setup.py", title="Setup (admin)", icon=":material/build:"),
    ],
    "30-minute lab": [
        st.Page("app_pages/s1_pipeline.py", title="1. The complaint", icon=":material/support_agent:"),
        st.Page("app_pages/s2_monitors.py", title="2. Put guards on it", icon=":material/shield:"),
        st.Page("app_pages/s3_diagnose.py", title="3. Catch, explain, contain", icon=":material/troubleshoot:"),
        st.Page("app_pages/s4_contain.py", title="4. Operate it", icon=":material/monitor_heart:"),
        st.Page("app_pages/stretch.py", title="Stretch: agents, digest, anomalies", icon=":material/rocket:"),
    ],
    "Bonus labs": [
        st.Page("app_pages/b1_cost.py", title="B1. Budgets and resource monitors", icon=":material/savings:"),
        st.Page("app_pages/b2_governance.py", title="B2. Governance and GDPR", icon=":material/policy:"),
        st.Page("app_pages/b3_dcm.py", title="B3. DevOps with DCM Projects", icon=":material/deployed_code:"),
    ],
    "Reference": [
        st.Page("app_pages/scaling.py", title="Rolling out to every operator", icon=":material/hub:"),
        st.Page("app_pages/availability.py", title="Azure UK South availability", icon=":material/public:"),
        st.Page("app_pages/coco_prompts.py", title="CoCo prompt cookbook", icon=":material/chat:"),
        st.Page("app_pages/coco_cheatsheet.py", title="CoCo cheat sheet", icon=":material/tips_and_updates:"),
        st.Page("app_pages/snowsight_map.py", title="Snowsight navigation map", icon=":material/map:"),
        st.Page("app_pages/troubleshooting.py", title="Troubleshooting", icon=":material/help:"),
        st.Page("app_pages/teardown.py", title="Teardown (admin)", icon=":material/delete_sweep:"),
    ],
}, position="sidebar")

st.sidebar.divider()
st.sidebar.image(str(_DIR / "static" / "gladstone_logo.jpg"), width=90)
st.sidebar.caption("Gladstone MRM - Data quality lab (Lite)")
st.sidebar.caption("GLADSTONE_DQ_LITE.RIVERSIDE_NIELS")
st.sidebar.info("This is a **read-only preview**. Results were captured from a real run of the lab. "
                "To run the exercises, use your own schema in Gladstone's Snowflake account and the interactive guide.",
                icon=":material/visibility:")

page.run()
