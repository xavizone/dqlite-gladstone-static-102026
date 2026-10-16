"""Headless render test of every page (run from the app folder: python tools/test_app.py)."""
from pathlib import Path

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parent.parent
bad = 0
for p in sorted((ROOT / "app_pages").glob("*.py")):
    at = AppTest.from_file(str(p), default_timeout=30)
    at.run()
    for b in at.button:                 # press reveal buttons (e.g. "Inject faults")
        b.click().run()
    md = " ".join(m.value for m in at.markdown)
    has_refs = "References" in md
    ok = not at.exception
    bad += (not ok) or (not has_refs)
    print(f"{'OK ' if ok else 'ERR'} {p.name:24s} refs={'y' if has_refs else 'n'} df={len(at.dataframe):2d} code={len(at.code):2d}"
          + (f"  {at.exception[0].message[:150]}" if at.exception else ""))
raise SystemExit(1 if bad else 0)
