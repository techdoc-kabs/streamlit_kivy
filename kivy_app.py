import streamlit as st
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(layout="wide")

# ---------- CSS to stop vertical collapsing ----------
st.markdown("""
    <style>
        /* Force horizontal alignment even on small screens */
        [data-testid="stHorizontalBlock"] {
            flex-wrap: wrap !important;
            flex-direction: row !important;
            justify-content: space-between;
        }
        [data-testid="column"] {
            min-width: 48% !important;  /* ensures 2 columns fit */
            flex: 1 1 48% !important;
        }

        /* For super small phones (≤320px) fallback to 1 col */
        @media (max-width: 320px) {
            [data-testid="column"] {
                min-width: 100% !important;
                flex: 1 1 100% !important;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ---------- Get screen width ----------
width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR")
if width is None:
    st.info("Resize the window to capture width...")
else:
    st.write(f"📏 Screen width detected: {width}px")

# ---------- Decide number of columns ----------
if width is None or width >= 992:
    cols = st.columns(3)
elif width >= 321:   # phones and tablets
    cols = st.columns(2)
else:                # tiny phones ≤320px
    cols = st.columns(1)

# ---------- Cards ----------
with cols[0]:
    st.markdown("### Card 1\nContent here...")
with cols[1]:
    st.markdown("### Card 2\nContent here...")
if len(cols) == 3:
    with cols[2]:
        st.markdown("### Card 3\nContent here...")

# ---------- Table ----------
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [24, 30, 28, 35],
    "Dept": ["HR", "IT", "Finance", "Marketing"]
})
st.dataframe(df, use_container_width=True)
