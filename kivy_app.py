import streamlit as st
import pandas as pd

st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# Optional: detect width
try:
    from streamlit_js_eval import streamlit_js_eval
    width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
except Exception:
    width = None

# ---------- Global CSS: container, cards, responsive table ----------
st.markdown(
    """
    <style>
    .cards-wrap {
      display: flex;
      gap: 12px;
      align-items: flex-start;
      justify-content: flex-start;
      flex-wrap: wrap;
      padding: 8px 0;
      box-sizing: border-box;
    }
    .card {
      background: #ffffff;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
      padding: 16px;
      min-width: 160px;
      flex: 0 0 32%;
      box-sizing: border-box;
      transition: transform 0.12s ease;
      overflow: hidden;
    }
    .card:hover { transform: translateY(-4px); }
    .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
    .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

    /* Table styling omitted for brevity (keep your original CSS) */

    @media (max-width: 992px) { .card { flex: 0 0 48%; } }
    @media (max-width: 768px) { .card { flex: 0 0 48%; padding: 12px; min-width: 140px; } }
    @media (max-width: 480px) { .card { flex: 0 0 48%; padding: 10px; min-width: 120px; } }
    @media (max-width: 320px) { .card { flex: 0 0 100%; min-width: 100%; } }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# ---------- Dynamic rendering: large vs small screen ----------
LARGE_SCREEN_THRESHOLD = 992
use_native_columns = False
if width is not None:
    st.write(f"📏 Detected browser width: {width}px")
    if width >= LARGE_SCREEN_THRESHOLD:
        use_native_columns = True
else:
    st.info("Screen width not detected — using responsive container.")

# ------------- Option A: Streamlit native columns (desktop) -------------
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

# ---------- Cards data ----------
cards = [
    {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
    {"title": "Analytics", "body": "Interactive charts and trends overview."},
    {"title": "Archives", "body": "Browse archived documents and files."},
    {"title": "Team", "body": "Quick team stats and availability."}
]

# ---------- Session-state clicked card ----------
if "clicked_card" not in st.session_state:
    st.session_state.clicked_card = None

# Only update clicked_card if session_state is empty
query_params = st.experimental_get_query_params()
if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
    st.session_state.clicked_card = query_params.get("nav")[0]

# ---------- Memoized function to build cards HTML ----------
# ---------- Memoized function to build cards HTML ----------
@st.cache_data
def get_cards_html(clicked=None):
    html = '<div class="cards-wrap">'
    for c in cards:
        highlight_style = "border: 2px solid #4CAF50;" if clicked == c["title"].lower() else ""
        html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
            <div class="card" style="{highlight_style}">
                <h3>{c["title"]}</h3>
                <p>{c["body"]}</p>
            </div>
        </a>
        '''
    html += "</div>"
    return html

# ---------- Page rendering ----------
if st.session_state.clicked_card is None:
    # Show cards menu
    st.title("Responsive Cards Menu")
    st.markdown(get_cards_html(), unsafe_allow_html=True)
else:
    # Show detailed card page
    st.title(f"{st.session_state.clicked_card.title()} Page")
    st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

    # Back button
    if st.button("⬅ Back to Menu"):
        st.session_state.clicked_card = None
        st.experimental_set_query_params()  # clear URL
        st.rerun()
