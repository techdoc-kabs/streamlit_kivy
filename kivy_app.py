import streamlit as st

# Define menu structure
MENUS = {
    "main": ["Consultations", "Reports", "Files", "Schedules"],
    "Consultations": ["New Session", "History"],
    "Schedules": ["Upcoming", "Past"]
}

# Get current page
params = st.query_params
current_page = params.get("page", "main")

# Back button
if current_page != "main":
    if st.button("⬅ Back", use_container_width=True):
        for parent, submenu in MENUS.items():
            if current_page in submenu:
                st.query_params["page"] = parent
                st.rerun()
        st.query_params["page"] = "main"
        st.rerun()

st.write(f"### {current_page}")

# ✅ Force 2-column layout using `st.columns`
buttons = MENUS[current_page]
for i in range(0, len(buttons), 2):
    cols = st.columns(2)
    for col, item in zip(cols, buttons[i:i+2]):
        if col.button(item, use_container_width=True):
            st.query_params["page"] = item
            st.rerun()
