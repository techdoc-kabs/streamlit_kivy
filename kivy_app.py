import streamlit as st

# Define Menus
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

# ✅ Custom CSS + HTML Buttons (Fully Responsive 2 Columns)
st.markdown("""
<style>
.button-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
}
.button-item {
    flex: 0 0 calc(50% - 12px);  /* ✅ Always 2 per row */
}
.custom-btn {
    background: #3498db;
    color: white;
    padding: 14px;
    border: none;
    width: 100%;
    border-radius: 8px;
    font-size: 16px;
    cursor: pointer;
    text-align: center;
}
.custom-btn:hover {
    background: #2980b9;
}
</style>
""", unsafe_allow_html=True)

st.write(f"### {current_page}")

# ✅ Render custom HTML buttons
st.markdown('<div class="button-grid">', unsafe_allow_html=True)
for item in MENUS[current_page]:
    st.markdown(f'''
        <div class="button-item">
            <button class="custom-btn" onclick="window.location.search='?page={item}'">{item}</button>
        </div>
    ''', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
