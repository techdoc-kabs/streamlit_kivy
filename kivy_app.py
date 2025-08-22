import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Responsive Layout", layout="wide")

# ---------- SIDEBAR TOGGLE ----------
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = True  # PC default open

def toggle_sidebar():
    st.session_state.sidebar_open = not st.session_state.sidebar_open

# Menu button at top
st.button("☰ Menu", on_click=toggle_sidebar)

# Sidebar content
if st.session_state.sidebar_open:
    with st.sidebar:
        st.header("Sidebar Menu")
        st.write("This is the sidebar content.")
        theme_choice = st.radio("Theme:", ["Light", "Dark"], index=0)

# ---------- THEME ADAPTATION ----------
if "theme" not in st.session_state:
    st.session_state.theme = "Light"

if "theme_choice" in locals():
    st.session_state.theme = theme_choice

bg_color = "#000000" if st.session_state.theme == "Dark" else "#FFFFFF"
text_color = "#FFFFFF" if st.session_state.theme == "Dark" else "#000000"

st.markdown(
    f"""
    <style>
    .main, .block-container, .stDataFrame {{
        background-color: {bg_color} !important;
        color: {text_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- SAMPLE DATA ----------
df = pd.DataFrame(
    {f"Col{i}": [f"Data {j}" for j in range(1, 6)] for i in range(1, 21)}  # 20 columns
)

# ---------- NORMAL TABLE ----------
st.subheader("Normal Table")
st.dataframe(df)

# ---------- AGGRID TABLE ----------
st.subheader("AgGrid Table")
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(resizable=True)
gb.configure_grid_options(domLayout='autoHeight')
gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, fit_columns_on_grid_load=True)
