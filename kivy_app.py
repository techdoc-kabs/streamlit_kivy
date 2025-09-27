import streamlit as st

# Define menus
MENUS = {
    "main": ["Consultations", "Reports", "Files", "Schedules"],
    "Consultations": ["New Session", "History"],
    "Schedules": ["Upcoming", "Past"]
}

# Get current page from session state
if "page" not in st.session_state:
    st.session_state.page = "main"

# Handle navigation
if "goto" in st.session_state:
    st.session_state.page = st.session_state.goto
    del st.session_state["goto"]
    st.experimental_rerun()

current_page = st.session_state.page

# Back button
if current_page != "main":
    if st.button("⬅ Back", use_container_width=True):
        for parent, submenu in MENUS.items():
            if current_page in submenu:
                st.session_state.page = parent
                st.experimental_rerun()
        st.session_state.page = "main"
        st.experimental_rerun()

st.write(f"### {current_page}")

# ✅ Force 2 columns using HTML <table>
html = "<table style='width:100%; text-align:center;'>"
buttons = MENUS[current_page]
for i in range(0, len(buttons), 2):
    html += "<tr>"
    for item in buttons[i:i+2]:
        html += f"""<td style='padding:8px;'>
            <form action="" method="post">
                <button name="goto" type="submit" value="{item}"
                    style="
                        background:#3498db; 
                        color:white;
                        padding:14px;
                        border:none;
                        border-radius:8px;
                        width:100%;
                        font-size:16px;
                        cursor:pointer;
                    ">{item}</button>
            </form>
        </td>
        """
    html += "</tr>"
html += "</table>"

st.markdown(html, unsafe_allow_html=True)
