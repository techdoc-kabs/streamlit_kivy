import streamlit as st
from st_aggrid import AgGrid
from streamlit_option_menu import option_menu
from streamlit_javascript import st_javascript
import pandas as pd
from PIL import Image

# ---- Detect screen width ----
screen_width = st_javascript("window.innerWidth") or 800

# ---- Detect current theme (light/dark) ----
theme = st.get_option("theme") or "light"

# ---- Set adaptive colors based on theme ----
if theme == "dark":
    background_color = "#0e1117"
    text_color = "#FFFFFF"
    table_header_color = "#1f1f1f"
    menu_selected_bg = "#1f1f1f"
else:
    background_color = "#FFFFFF"
    text_color = "#000000"
    table_header_color = "#f0f0f0"
    menu_selected_bg = "#0d6efd"

# ---- Adaptive font size ----
if screen_width < 600:
    font_size = 14
elif screen_width < 900:
    font_size = 18
else:
    font_size = 24

# ---- Inject CSS for theme and sidebar ----
st.markdown(f"""
<style>
/* Body background and text */
body {{
    background-color: {background_color};
    color: {text_color};
}}
/* Force sidebar width */
.css-1d391kg {{
    min-width: 250px !important;
}}
@media screen and (max-width: 600px){{
    .css-1d391kg {{min-width: 200px !important;}}
}}
/* Sidebar font */
.sidebar-text {{
    font-size: {font_size}px;
}}
/* Table header */
.ag-header-cell-label {{
    background-color: {table_header_color} !important;
    color: {text_color} !important;
}}
</style>
""", unsafe_allow_html=True)

# ---- Sidebar toggle button (hamburger) ----
menu_clicked = st.button("☰ Menu")
if menu_clicked:
    st_javascript("""
        const sidebar = window.parent.document.querySelector('div[data-testid="stSidebar"]');
        if (sidebar) sidebar.style.display = (sidebar.style.display === 'none') ? 'block' : 'none';
    """)

# ---- Sidebar content ----
if screen_width < 600:
    st.selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])
else:
    st.sidebar.selectbox("Choose option", ["Option 1", "Option 2", "Option 3"])
st.sidebar.slider("Select value", 0, 100)

# ---- Responsive option menu ----
orientation = "vertical" if screen_width < 600 else "horizontal"
menu_styles = {
    "container": {"width": "100%"},
    "nav-link": {"font-size": f"{font_size}px", "text-align": "center", "color": text_color},
    "nav-link-selected": {"background-color": menu_selected_bg}
}
selected = option_menu(
    menu_title=None,
    options=["Home", "Settings", "Profile"],
    icons=["house", "gear", "person"],
    menu_icon="cast",
    default_index=0,
    orientation=orientation,
    styles=menu_styles
)
st.markdown(f"<p style='font-size:{font_size}px; color:{text_color}'>You selected: {selected}</p>", unsafe_allow_html=True)

# ---- Responsive table ----
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Score": [95, 87, 78, 92],
    "Remarks": ["Excellent", "Good", "Average", "Very Good"]
})
st.markdown(f"<p style='font-size:{font_size}px; color:{text_color}'>Student Scores:</p>", unsafe_allow_html=True)
AgGrid(df, fit_columns_on_grid_load=True)

# ---- Responsive image ----
# Replace these with images suitable for light/dark themes
img_path = "example_dark.jpg" if theme == "dark" else "example_light.jpg"
img = Image.open(img_path)
st.markdown(f"<p style='font-size:{font_size}px; color:{text_color}'>Example Image:</p>", unsafe_allow_html=True)
st.image(img, use_column_width=True)
