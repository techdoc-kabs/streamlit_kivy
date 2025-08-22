import streamlit as st

st.set_page_config(page_title="Sidebar Toggle", layout="wide")

st.title("Custom Sidebar Toggle Button")

# Sidebar content
with st.sidebar:
    st.header("Sidebar Menu")
    st.write("Some menu content here...")

# Add Hamburger icon using HTML + JS
st.markdown("""
    <style>
    .menu-button {
        background: none;
        border: none;
        cursor: pointer;
        padding: 5px;
        margin: 0;
        position: fixed;
        top: 15px;
        left: 15px;
        z-index: 9999;
    }
    .menu-icon {
        width: 25px;
        height: 3px;
        background-color: black;
        margin: 5px 0;
        border-radius: 2px;
    }
    </style>

    <button class="menu-button" onclick="toggleSidebar()">
        <div class="menu-icon"></div>
        <div class="menu-icon"></div>
        <div class="menu-icon"></div>
    </button>

    <script>
    function toggleSidebar() {
        // Find the real Streamlit sidebar toggle button and click it
        const sidebarToggle = window.parent.document.querySelector('[data-testid="stSidebarCollapseButton"]');
        if (sidebarToggle) {
            sidebarToggle.click();
        }
    }
    </script>
""", unsafe_allow_html=True)
