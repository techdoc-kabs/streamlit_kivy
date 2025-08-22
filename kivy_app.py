import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd

# Page config
st.set_page_config(page_title="Responsive Layout with Sidebar", layout="wide")

# Sample Data for both Table and AgGrid
data = {
    "Name": ["Paul", "Alice", "John", "Grace", "David"],
    "Age": [25, 30, 22, 28, 35],
    "Country": ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"],
    "Occupation": ["Doctor", "Engineer", "Teacher", "Nurse", "Lawyer"]
}
df = pd.DataFrame(data)

# ---- Sidebar Toggle Button ----
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = True

def toggle_sidebar():
    st.session_state.show_sidebar = not st.session_state.show_sidebar

# Place menu button at top
st.button("☰ Menu", on_click=toggle_sidebar)

# Sidebar content
if st.session_state.show_sidebar:
    with st.sidebar:
        st.header("Sidebar Content")
        st.write("You can put filters or menus here")
        theme_choice = st.radio("Select Theme", ["Light", "Dark"])
else:
    st.write("Sidebar is collapsed. Click ☰ Menu to open it.")

# ---- Main Layout ----
st.subheader("Responsive Table vs AgGrid Table")

# Show normal Streamlit Table
st.write("### Streamlit Table")
st.dataframe(df)

# Show AgGrid Table
st.write("### AgGrid Table")
gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(resizable=True, wrapText=True, autoHeight=True)
gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, height=200, fit_columns_on_grid_load=True)

# ---- Columns Section (20 columns to test responsiveness) ----
st.write("### 20 Responsive Columns")
cols = st.columns(20)
for i, col in enumerate(cols):
    col.metric(label=f"Column {i+1}", value=f"Val {i+1}")
