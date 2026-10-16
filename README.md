# Gladstone MRM | Data quality lab (Lite) | Static backup

A read-only copy of the Lite lab guide for streamlit.io. **No Snowflake connection.** Every result shown was
captured from a real run of the lab on a Snowflake demo account (16 Oct 2026); account and user identifiers are
replaced with placeholders, and all data is synthetic.

Use it when the live guide or the lab account isn't available, or to preview the lab before the day.

## Run locally

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Deploy to Streamlit Community Cloud

1. Push this repository to GitHub.
2. At share.streamlit.io choose **Create app** » this repository » branch `main` » main file `streamlit_app.py`.
3. No secrets are needed.

## What's inside

| Path | What |
|---|---|
| `streamlit_app.py` | Entry point and navigation |
| `app_pages/` | Overview, Sessions 1-4, stretch, bonus B1-B3, reference pages |
| `sample_data.py` | Results captured from the real run (generated) |
| `snippets.py` | Prompts, SQL and Snowsight routes copied from the live guide (generated) |
| `ui.py`, `components.py` | Shared layout helpers; `components.py` lets reference pages from the live guide render unchanged |
| `sql/` | The same SQL scripts as the live lab |
| `*.md`, `*.csv` | Hand-outs: attendee prep, admin questionnaire, run sheet, roster template, leave-behind |
| `tools/test_app.py` | Headless smoke test of every page |
