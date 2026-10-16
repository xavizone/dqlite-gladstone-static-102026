# CoCo prompt cookbook - every lab prompt in one place
# Co-authored with CoCo
import streamlit as st

import links as L
from components import render_real_world_examples, render_references
from snippets import PAGES

st.title("CoCo prompt cookbook")
st.info("""**Capability:** CoCo (Cortex Code) turns plain-English data quality requests into Snowflake SQL, explains it,
and runs it after your approval. Every step in this lab is one prompt.

**How to use:** paste a prompt into CoCo Desktop or the CoCo CLI. Replace `RIVERSIDE_NIELS` with your schema.""",
        icon=":material/chat:")

SECTIONS = [("session_01", "1. The complaint"), ("session_02", "2. Put guards on it"),
            ("session_03", "3. Catch, explain, contain"), ("session_04", "4. Operate it"),
            ("stretch", "Stretch: agents, digest, anomalies"),
            ("bonus_b1", "B1. Budgets and resource monitors"), ("bonus_b2", "B2. Governance and GDPR"),
            ("bonus_b3", "B3. DevOps with DCM Projects")]

st.markdown("| Section | Prompts |\n|---|---|\n" + "\n".join(
    f"| {label} | " + ", ".join(f"{p['id'].replace('Prompt ', '')} {p['title']}" for p in PAGES[k]["prompts"]) + " |"
    for k, label in SECTIONS))

for key, label in SECTIONS:
    with st.expander(f"**{label}**", expanded=False):
        for p in PAGES[key]["prompts"]:
            st.markdown(f"**{p['id']} - {p['title']}**")
            st.code(p["text"], language="text", wrap_lines=True)

render_real_world_examples([
    {"title": "Support playbook", "body": "Save these prompts as a CoCo skill so every CS and data engineer investigates an operator the same way."},
    {"title": "Scripted fleet checks", "body": "Run the same prompts with the CoCo CLI against several operator databases from a terminal or a scheduled job."},
])
render_references({
    "Quickstarts": [L.QS_COCO_BP, L.QS_COCO_DE, L.QS_COCO_CLI],
    "Docs": [L.COCO, L.COCO_CLI, L.DQ_DASH],
})
