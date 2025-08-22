import streamlit as st

st.set_page_config(page_title="Sidebar Toggle Button", layout="wide")

# Inject JavaScript to trigger the real Streamlit sidebar arrow
toggle_sidebar = """
<script>
function toggleSidebar() {
    const sidebarButton = window.parent.document.querySelector('[data-testid="collapsedControl"]');
    if (sidebarButton) {
        sidebarButton.click();
    }
}
</script>
"""

# Place the JS in the app
st.markdown(toggle_sidebar, unsafe_allow_html=True)

# Button that calls the JavaScript function
st.markdown(
    '<button onclick="toggleSidebar()" style="font-size:18px; padding:5px 10px; cursor:pointer;">☰ Menu</button>',
    unsafe_allow_html=True
)

# Main page content
st.title("Main Page")
st.write("Click ☰ Menu to toggle the real sidebar arrow")
