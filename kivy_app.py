import streamlit as st
import pandas as pd
from streamlit_js_eval import streamlit_js_eval

st.set_page_config(layout="wide")

# --- Get browser width ---
width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR")
if width is None:
    st.info("Resize the window to capture width...")
else:
    st.write(f"📏 Screen width detected: {width}px")

# --- Decide number of columns dynamically ---
if width is None or width >= 992:
    cols = st.columns(3)
elif width >= 481:
    cols = st.columns(2)
else:
    cols = st.columns(2)

with cols[0]:
    st.markdown("### Card 1\nContent here...")
with cols[1]:
    st.markdown("### Card 2\nContent here...")
if len(cols) == 3:
    with cols[2]:
        st.markdown("### Card 3\nContent here...")

# --- Responsive Table ---
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [24, 30, 28, 35],
    "Dept": ["HR", "IT", "Finance", "Marketing"]
})
st.dataframe(df, use_container_width=True)
