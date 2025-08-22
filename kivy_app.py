import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode, DataReturnMode

# ---------- Detect system theme ----------
if "theme" not in st.session_state:
    st.session_state.theme = "light"

system_theme = st.get_option("theme.base")
if system_theme == "dark":
    st.session_state.theme = "dark"
else:
    st.session_state.theme = "light"

# ---------- Page config ----------
st.set_page_config(
    page_title="Adaptive Layout Demo",
    layout="wide",
    initial_sidebar_state="expanded" if st.session_state.theme == "light" else "collapsed"
)

# ---------- Sidebar manual toggle ----------
with st.sidebar:
    st.image("paul.jpg", use_column_width=True)
    st.title("Sidebar Menu")
    st.write("Toggle me manually on mobile!")
    theme_choice = st.radio("Choose AgGrid Theme", ["streamlit", "alpine", "balham", "material"])

# ---------- Sample Data with 20 columns ----------
data = {f"Col{i}": [f"Data {i}-{j}" for j in range(1, 6)] for i in range(1, 21)}
df = pd.DataFrame(data)

# ---------- Option Menu Style Adaptation ----------
menu_style = {
    "backgroundColor": "#000" if st.session_state.theme == "dark" else "#fff",
    "color": "#fff" if st.session_state.theme == "dark" else "#000",
    "padding": "10px",
    "borderRadius": "8px"
}

st.markdown(
    f"<div style='background-color:{menu_style['backgroundColor']};"
    f"color:{menu_style['color']}; padding:10px; border-radius:8px; text-align:center;'>"
    f"**Main Content Area with Adaptive Theme**</div>", unsafe_allow_html=True
)

# ---------- Normal Streamlit Table ----------
st.subheader("Normal Streamlit Table")
st.dataframe(df, use_container_width=True)

# ---------- AgGrid Table with Responsiveness ----------
st.subheader("AgGrid Table (Responsive)")
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(enabled=True)
gb.configure_side_bar()
gb.configure_default_column(
    resizable=True, wrapHeaderText=True, autoHeaderHeight=True
)
gb.configure_grid_options(domLayout='autoHeight')
grid_options = gb.build()

AgGrid(
    df,
    gridOptions=grid_options,
    theme=theme_choice,
    enable_enterprise_modules=False,
    data_return_mode=DataReturnMode.FILTERED_AND_SORTED,
    update_mode=GridUpdateMode.NO_UPDATE,
    fit_columns_on_grid_load=False,
    height=300,
    allow_unsafe_jscode=True,
    reload_data=True
)
