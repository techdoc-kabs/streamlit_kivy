import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sidebar Toggle Demo", layout="wide")

st.title("Custom Sidebar Toggle with Hamburger Menu")

# Sidebar content
with st.sidebar:
    st.header("Sidebar Menu")
    st.write("Your sidebar content goes here")

# Add custom hamburger menu button with CSS
st.markdown("""
    <style>
    .menu-button {
        background: none;
        border: none;
        cursor: pointer;
        padding: 8px;
        margin: 0;
        position: fixed;
        top: 15px;
        left: 15px;
        z-index: 9999;
    }
    .menu-icon {
        width: 25px;
        height: 3px;
        background-color: #333;
        margin: 5px 0;
        border-radius: 2px;
        transition: 0.4s;
    }
    </style>

    <button class="menu-button" onclick="toggleSidebar()">
        <div class="menu-icon"></div>
        <div class="menu-icon"></div>
        <div class="menu-icon"></div>
    </button>

    <script>
    function toggleSidebar() {
        const sidebarToggle = window.parent.document.querySelector('button[title="Collapse sidebar"]');
        if (sidebarToggle) {
            sidebarToggle.click();
        }
    }
    </script>
""", unsafe_allow_html=True)
