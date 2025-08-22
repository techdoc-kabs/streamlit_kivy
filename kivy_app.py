import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder
import pandas as pd
from streamlit_option_menu import option_menu
import base64

# ------------------ Detect Dark/Light Mode ------------------
def get_theme():
    return st.session_state.get("theme", "light")

# JS to detect system theme
st.markdown("""
    <script>
    const theme = window.matchMedia('(prefers-color-scheme: dark)').matches ? "dark" : "light";
    window.parent.postMessage({theme: theme}, "*");
    </script>
""", unsafe_allow_html=True)

# ------------------ Sidebar Toggle Button ------------------
menu_btn = st.button("☰ Menu", key="menu_btn")
if menu_btn:
    st.session_state["sidebar_open"] = not st.session_state.get("sidebar_open", True)

if st.session_state.get("sidebar_open", True):
    with st.sidebar:
        st.markdown("### Sidebar Menu")
        st.markdown("Adaptive font sizes & dark mode support")

# ------------------ Option Menu ------------------
selected = option_menu(
    menu_title=None,
    options=["Home", "Dashboard", "Reports", "Settings", "Help"],
    icons=["house", "bar-chart", "file-text", "gear", "question-circle"],
    orientation="horizontal",
)

# ------------------ Adaptive Layout ------------------
theme = get_theme()
bg_color = "#1E1E1E" if theme == "dark" else "#FFFFFF"
font_color = "#FFFFFF" if theme == "dark" else "#000000"

st.markdown(
    f"""
    <style>
    .main-container {{
        background-color: {bg_color};
        color: {font_color};
        transition: all 0.3s ease;
    }}
    .stApp {{
        background-color: {bg_color};
    }}
    .stButton > button {{
        color: {font_color};
    }}
    .nav-link {{
        color: {font_color} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Image ------------------
st.image("paul.jpg", use_column_width=True)

# ------------------ DataFrame with AgGrid ------------------
data = {
    "Name": ["Paul", "John", "Mary", "Anna", "James"],
    "Age": [25, 30, 22, 28, 35],
    "City": ["Kampala", "Gulu", "Mbarara", "Entebbe", "Jinja"],
    "Score": [85, 90, 78, 92, 88],
    "Grade": ["B", "A", "C", "A", "B"]
}
df = pd.DataFrame(data)

gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_pagination(paginationAutoPageSize=True)
gb.configure_side_bar()
gb.configure_default_column(resizable=True, wrapText=True, autoHeight=True)
gridOptions = gb.build()

AgGrid(df, gridOptions=gridOptions, height=300, theme="dark" if theme == "dark" else "light")

# ------------------ Columns Test ------------------
st.markdown("### 5-Column Layout Test")
cols = st.columns(5)
for i, col in enumerate(cols):
    col.markdown(f"**Column {i+1}**")
    col.write("Content adapts to screen size")
