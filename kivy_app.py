import streamlit as st

# Define Menus
MENUS = {
    "main": ["Consultations", "Reports", "Files", "Schedules"],
    "Consultations": ["New Session", "History"],
    "Schedules": ["Upcoming", "Past"]
}

# Get page state
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

# ✅ CSS Flexbox to Force 2-Column Layout
st.markdown("""
<style>
.button-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}
.button-grid > div {
    flex: 0 0 calc(50% - 10px);  /* ✅ Forces 2 columns always */
}
</style>
""", unsafe_allow_html=True)

st.write(f"### {current_page}")

# ✅ Render Buttons inside Flexbox Containers
st.markdown('<div class="button-grid">', unsafe_allow_html=True)

for item in MENUS[current_page]:
    # Each button is wrapped in its own div
    st.markdown('<div>', unsafe_allow_html=True)
    if st.button(item, key=item, use_container_width=True):
        st.query_params["page"] = item
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
