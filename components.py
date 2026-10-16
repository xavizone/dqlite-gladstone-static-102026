# Compatibility shim so reference pages copied from the live guide render unchanged in the static app
# Co-authored with CoCo
from pathlib import Path

import streamlit as st

SQL_DIR = Path(__file__).resolve().parent / "sql"
CTX = {"NAME": "NIELS", "SCHEMA": "RIVERSIDE_NIELS", "FQ_SCHEMA": "GLADSTONE_DQ_LITE.RIVERSIDE_NIELS",
       "ROLE": "DQ_LITE_ATTENDEE", "DB": "GLADSTONE_DQ_LITE", "WH": "DQ_LITE_WH"}


def ctx() -> dict:
    return dict(CTX)


def fill(text: str) -> str:
    for k, v in CTX.items():
        text = text.replace("{" + k + "}", v)
    return text


def sql_file(rel_path: str) -> str:
    return (SQL_DIR / rel_path).read_text()


def render_sql_file(rel_path: str, label: str | None = None, expanded: bool = False):
    with st.expander(label or f":material/description: `{rel_path}`", expanded=expanded):
        st.code(sql_file(rel_path), language="sql", line_numbers=True)


def render_real_world_examples(items: list[dict]):
    st.divider()
    with st.expander(":material/apartment: Real-world use cases at Gladstone", expanded=False):
        for it in items:
            st.markdown(f"- **{it['title']}** - {it['body']}")


def render_references(links: dict):
    from links import VERIFIED_ON

    st.markdown("##### :material/menu_book: References")
    for group, items in links.items():
        if not items:
            continue
        st.markdown(f"**{group}**")
        for title, url, note in items:
            st.markdown(f"- [{title}]({url})" + (f" - {note}" if note else ""))
    st.caption(f"Links verified {VERIFIED_ON}.")


DOC_DIR = Path(__file__).resolve().parent


def doc_file(name: str) -> str:
    p = DOC_DIR / name
    return p.read_text() if p.exists() else f"{name} not found"


def render_doc_download(name: str, label: str, mime: str = "text/markdown"):
    st.download_button(label, data=doc_file(name), file_name=name, mime=mime,
                       icon=":material/download:", key=f"dl_{name}")
