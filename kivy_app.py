# app.py
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# Optional: try to detect width using streamlit-js-eval (not required)
try:
    from streamlit_js_eval import streamlit_js_eval
    width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
except Exception:
    width = None

# ---------- Global CSS: container, cards, responsive table ----------
st.markdown(
    """
    <style>
    /* ---------- Container + Cards ---------- */
    .cards-wrap {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;               /* allow wrapping */
      padding: 8px 0;
      box-sizing: border-box;
    }

    .card {
      background: #ffffff;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
      padding: 16px;
      min-width: 160px;             /* prevents cards from going too narrow */
      flex: 0 0 32%;                /* desktop: ~3 per row */
      box-sizing: border-box;
      transition: transform 0.12s ease;
      overflow: hidden;
    }
    .card:hover { transform: translateY(-4px); }
    .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
    .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

    /* ---------- Table ---------- */
    .resp-table { width:100%; border-collapse: collapse; margin-top: 8px; }
    .resp-table th, .resp-table td { padding: 8px 10px; border: 1px solid #e6e6e6; text-align:left; font-size:14px; }
    .resp-table th { background:#0d1b3d; color:#fff; }

    /* ---------- Breakpoints ---------- */
    /* Tablet-ish: 3->2 */
    @media (max-width: 992px) {
      .card { flex: 0 0 48%; }      /* 2 cards per row */
    }

    /* Phones: ensure 2 columns side-by-side down to 321px */
    @media (max-width: 768px) {
      .card { flex: 0 0 48%; padding: 12px; min-width: 140px; }
      .cards-wrap { gap: 8px; }
      .resp-table th, .resp-table td { font-size:13px; padding: 6px 8px; }
    }

    /* Very small phones but still bigger than tiny: keep 2 col behavior */
    @media (max-width: 480px) {
      .card { flex: 0 0 48%; padding: 10px; min-width: 120px; }
      .card h3 { font-size: 14px; }
      .card p { font-size: 12px; }
      .resp-table th, .resp-table td { font-size:12px; }
    }

    /* TINY phones (<= 320px) -> fallback to single column */
    @media (max-width: 320px) {
      .card { flex: 0 0 100%; min-width: 100%; }
      .cards-wrap { gap: 6px; }
      .card h3 { font-size: 13px; }
      .card p { font-size: 11px; }
    }

    /* ---------- Responsive table -> stacked rows on tiny screens ---------- */
    @media (max-width: 480px) {
      .resp-table, .resp-table thead, .resp-table tbody, .resp-table th, .resp-table td, .resp-table tr {
        display: block;
        width: 100%;
      }
      .resp-table thead { display: none; } /* hide table header on small screens */
      .resp-table tr { margin-bottom: 12px; border: 1px solid #eee; padding: 8px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.03); }
      .resp-table td { display: flex; justify-content: space-between; padding: 8px 10px; }
      .resp-table td:before { content: attr(data-label); font-weight:600; margin-right:8px; color:#555; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# ---------- Dynamic rendering: use Streamlit native columns on large screens, custom container on smaller screens ----------
LARGE_SCREEN_THRESHOLD = 992
SMALL_SINGLE_COL_THRESHOLD = 320

use_native_columns = False
if width is not None:
    st.write(f"📏 Detected browser width: {width}px")
    if width >= LARGE_SCREEN_THRESHOLD:
        use_native_columns = True
else:
    # width unknown: default to custom container (safe)
    st.info("Screen width not detected — using responsive container (recommended).")

# ------------- Option A: Streamlit native columns (desktop - optional) -------------
if use_native_columns:
    st.subheader("Native Streamlit columns (desktop)")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Metric A", "120")
        st.write("Description A")
    with c2:
        st.metric("Metric B", "72")
        st.write("Description B")
    with c3:
        st.metric("Metric C", "45")
        st.write("Description C")
    st.markdown("---")

# ------------- Option B: Custom HTML Container for cards (mobile-friendly) -------------
st.subheader("Cards (custom container — controlled by our CSS)")
cards = [
    {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
    {"title": "Analytics", "body": "Interactive charts and trends overview."},
    {"title": "Archives", "body": "Browse archived documents and files."},
    {"title": "Team", "body": "Quick team stats and availability."}
]

# Build HTML for cards
cards_html = '<div class="cards-wrap">'
for c in cards:
    cards_html += f'''<div class="card">
        <h3>{c["title"]}</h3>
        <p>{c["body"]}</p>
      </div>
    '''
cards_html += "</div>"

st.markdown(cards_html, unsafe_allow_html=True)

# ---------- Responsive Table (HTML) ----------
st.title("Responsive Table (columns fit screen)")

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana","kimera", "peter", "robert"],
    "Age": [24, 30, 28, 35, 36, 37, 38],
    "Department": ["HR", "IT", "Finance", "Marketing", 'computing", "biology", "Agriculture"],
    "Position": ["Manager", "Developer", "Analyst", "Designer", "Developer", "Analyst", "Designer"]
})

# CSS for responsive table (fits screen)
st.markdown("""
    <style>
    .resp-table-fixed {
        width: 100% !important;
        border-collapse: collapse;
        table-layout: fixed; /* ensures columns shrink to fit */
    }
    .resp-table-fixed th, .resp-table-fixed td {
        padding: 8px 10px;
        border: 1px solid #ddd;
        overflow-wrap: break-word; /* wrap long content */
        text-align: left;
        font-size: 14px;
    }
    .resp-table-fixed th {
        background-color: #0d1b3d;
        color: white;
    }

    /* Optional: smaller font on mobile */
    @media (max-width: 768px) {
        .resp-table-fixed th, .resp-table-fixed td {
            font-size: 12px;
            padding: 6px 8px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Render table as HTML
table_html = '<table class="resp-table-fixed">'
table_html += '<thead><tr>' + ''.join(f'<th>{col}</th>' for col in df.columns) + '</tr></thead>'
table_html += '<tbody>'
for _, row in df.iterrows():
    table_html += '<tr>' + ''.join(f'<td>{row[col]}</td>' for col in df.columns) + '</tr>'
table_html += '</tbody></table>'

st.markdown(table_html, unsafe_allow_html=True)

