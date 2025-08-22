import streamlit as st

st.set_page_config(page_title="Custom Sidebar Toggle", layout="wide")

# State for sidebar visibility
if "show_sidebar" not in st.session_state:
    st.session_state.show_sidebar = True

# Main page button to toggle sidebar
if st.button("☰ Menu"):
    st.session_state.show_sidebar = not st.session_state.show_sidebar

# Show sidebar content only if state is True
if st.session_state.show_sidebar:
    with st.sidebar:
        st.header("Sidebar Menu")
        st.write("This is your sidebar content...")
        st.button("Option 1")
        st.button("Option 2")

# Main page content
st.title("Main Page")
st.write("Click ☰ Menu to toggle the sidebar")
