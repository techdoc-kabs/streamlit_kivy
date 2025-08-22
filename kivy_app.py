import streamlit as st
from streamlit_javascript import st_javascript

# Add a menu button
if "sidebar_open" not in st.session_state:
    st.session_state.sidebar_open = False

# JavaScript to toggle sidebar visibility
toggle_sidebar_js = """
() => {
    const sidebar = window.parent.document.querySelector("section[data-testid='stSidebar']");
    const collapseButton = window.parent.document.querySelector("button[title='Close sidebar']");
    if (sidebar && collapseButton) {
        collapseButton.click();
    }
}
"""

st.markdown("<h1>Main Page Content</h1>", unsafe_allow_html=True)

# Custom menu button
if st.button("☰ Menu"):
    st_javascript(toggle_sidebar_js)
