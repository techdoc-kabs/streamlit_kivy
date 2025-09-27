import streamlit as st

# -------------------- MENUS --------------------
MENUS = {
    "main": ["Consultations", "Reports", "Files", "Schedules"],
    "Consultations": ["New Session", "History"],
    "Schedules": ["Upcoming", "Past"]
}

# -------------------- Navigation --------------------
# Get current page from query params
current_page = st.session_state.get("current_page")
if not current_page:
    current_page = st.query_params.get("page", ["main"])[0]
    st.session_state.current_page = current_page

# Back button
if current_page != "main":
    if st.button("⬅ Back"):
        # Find parent page
        parent = "main"
        for k, v in MENUS.items():
            if current_page in v:
                parent = k
        st.session_state.current_page = parent
        st.experimental_set_query_params(page=parent)
        st.rerun()

st.write(f"### {current_page}")

# -------------------- Two-column layout --------------------
buttons = MENUS.get(current_page, [])
cols = st.columns(2)

for i, item in enumerate(buttons):
    col = cols[i % 2]
    if col.button(item, key=f"{current_page}-{item}"):
        st.session_state.current_page = item
        st.experimental_set_query_params(page=item)
        st.rerun()
