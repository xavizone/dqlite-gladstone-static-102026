# Shared building blocks for the static (read-only) Gladstone DQ lab - Clutch static style
# Co-authored with CoCo
import pandas as pd
import streamlit as st

from snippets import PAGES

LIVE_GUIDE = "the interactive lab guide (ask your facilitator for the link)"


def capability(text: str, used_in: str, confirm: str):
    st.info(f"""**Capability:** {text}

**Used in:** {used_in} | **Confirm on Azure UK South:** {confirm}""", icon=":material/info:")


def why_what_outcome(why: str, what: list[str], outcome: str):
    st.markdown("### Why this matters")
    st.markdown(why)
    st.markdown("### What we'll demonstrate")
    st.markdown("\n".join(f"{i}. {w}" for i, w in enumerate(what, 1)))
    st.markdown("### Outcome")
    st.markdown(outcome)


def what_why(page: str):
    p = PAGES[page]
    if "what" not in p:
        return
    c1, c2 = st.columns(2)
    with c1.container(border=True, height="stretch"):
        st.markdown("##### :material/flag: What")
        st.markdown(p["what"])
    with c2.container(border=True, height="stretch"):
        st.markdown("##### :material/lightbulb: Why it matters for Gladstone")
        st.markdown(p["why"])


def header(page: str):
    h = PAGES[page].get("header")
    if h:
        st.title(f"{h['label']}: {h['title']}")
        c1, c2 = st.columns(2)
        c1.markdown(f":material/schedule: **{h['duration']}**")
        c2.markdown(f":material/construction: **Building**: {h['building']}")


def table(rows, caption: str | None = None, cols: list[str] | None = None):
    df = pd.DataFrame(rows)
    if cols:
        df = df[[c for c in cols if c in df.columns]]
    st.dataframe(df, hide_index=True, width="stretch")
    if caption:
        st.caption(caption)


def result_label(text: str = "Captured from a real run"):
    st.caption(f":material/history: {text} - schema `RIVERSIDE_NIELS` unless stated. Read-only preview.")


def prompt(page: str, idx: int):
    p = PAGES[page]["prompts"][idx]
    with st.container(border=True):
        st.markdown(f"#### :material/terminal: {p['id']} - {p['title']}")
        st.caption("Paste into CoCo Desktop or the CoCo CLI (schema shown as RIVERSIDE_NIELS)")
        st.code(p["text"], language="text", wrap_lines=True)


def snowsight(page: str, idx: int):
    """Snowsight route(s) that follow prompt number idx in the live guide."""
    pid = PAGES[page]["prompts"][idx]["id"]
    for r in [r for r in PAGES[page]["snowsight"] if r.get("after") == pid]:
        with st.expander(":material/web: Do it in Snowsight", expanded=False):
            for i, s in enumerate(r["steps"], 1):
                st.markdown(f"{i}. {s}")
            if r["sql"]:
                st.code(r["sql"], language="sql")


def step(page: str, idx: int):
    """Prompt + its Snowsight route + any checkpoint that follows it."""
    prompt(page, idx)
    snowsight(page, idx)
    pid = PAGES[page]["prompts"][idx]["id"]
    for c in [c for c in PAGES[page]["checkpoints"] if c.get("after") == pid]:
        with st.container(border=True):
            st.markdown(f":material/task_alt: **Checkpoint** - {c['text']}")
            if c["sql"]:
                st.code(c["sql"], language="sql")


def sql_steps(page: str, title: str = "Step-by-step SQL (what CoCo generates)"):
    fbs = PAGES[page]["fallbacks"]
    if not fbs:
        return
    st.divider()
    st.subheader(title)
    for fb in fbs:
        st.code(fb, language="sql")


def checkpoints(page: str):
    for c in PAGES[page]["checkpoints"]:
        with st.container(border=True):
            st.markdown(f":material/task_alt: **Checkpoint** - {c['text']}")
            if c["sql"]:
                st.code(c["sql"], language="sql")


def explanations(page: str):
    for e in PAGES[page]["explanations"]:
        with st.expander(f":material/school: {e['title']}"):
            st.markdown(e["body"])


def tech(page: str):
    t = PAGES[page].get("tech")
    if not t:
        return
    st.markdown("##### :material/build: Snowflake capabilities in this section")
    cols = st.columns(min(len(t), 3))
    for i, x in enumerate(t):
        with cols[i % len(cols)].container(border=True, height="stretch"):
            st.markdown(f":material/{x.get('icon', 'widgets')}: **{x['name']}**")
            st.caption(x["description"])


def footer(page: str):
    """Clutch-style use-case expander + the same verified references as the live guide."""
    from links import VERIFIED_ON

    p = PAGES[page]
    st.divider()
    if p["examples"]:
        with st.expander(":material/apartment: Real-world use cases at Gladstone", expanded=False):
            for ex in p["examples"]:
                st.markdown(f"- **{ex['title']}** - {ex['body']}")
    if p["refs"]:
        st.markdown("##### :material/menu_book: References")
        for group, items in p["refs"].items():
            if not items:
                continue
            st.markdown(f"**{group}**")
            for title, url, note in items:
                st.markdown(f"- [{title}]({url})" + (f" - {note}" if note else ""))
        st.caption(f"Links verified {VERIFIED_ON}.")


def expectations_table(rows):
    df = pd.DataFrame(rows)
    keep = [c for c in ["METRIC_NAME", "EXPECTATION_NAME", "EXPECTATION_EXPRESSION", "VALUE", "EXPECTATION_VIOLATED"] if c in df.columns]
    df = df[keep].rename(columns={"EXPECTATION_VIOLATED": "VIOLATED"})
    st.dataframe(df, hide_index=True, width="stretch",
                 column_config={"VIOLATED": st.column_config.CheckboxColumn("Violated")})
