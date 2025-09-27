import streamlit as st

# -------------------- MENUS --------------------
MENUS = {
    "main": [
        {"label": "Consultations", "icon": "👨‍⚕️"},
        {"label": "Reports", "icon": "📚"},
        {"label": "Files", "icon": "🗂️"},
        {"label": "Schedules", "icon": "📅"},
    ],
    "Consultations": [
        {"label": "New Session", "icon": "🆕"},
        {"label": "History", "icon": "📜"}
    ],
    "Schedules": [
        {"label": "Upcoming", "icon": "⏳"},
        {"label": "Past", "icon": "✅"}
    ]
}

# -------------------- Styling --------------------
CARD_CSS = """
<style>
.card-container {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
}
.card {
    flex: 1 1 48%;
    max-width: 48%;
    background-color: #4CAF50;
    color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
}
.card-icon {
    font-size: 32px;
    margin-bottom: 8px;
}
@media (max-width: 600px){
    .card { flex: 1 1 48%; max-width: 48%; }  /* still 2 columns on small screens */
}
</style>
"""
st.markdown(CARD_CSS, unsafe_allow_html=True)

# -------------------- Session State --------------------
if "nav_stack" not in st.session_state:
    st.session_state.nav_stack = ["main"]

current_page = st.session_state.nav_stack[-1]

# -------------------- Back Button --------------------
if len(st.session_state.nav_stack) > 1:
    if st.button("⬅ Back"):
        st.session_state.nav_stack.pop()
        current_page = st.session_state.nav_stack[-1]
        st.rerun()

st.write(f"### {current_page}")

# -------------------- Display Cards --------------------
buttons = MENUS.get(current_page, [])
cols = st.columns(2)

for i, item in enumerate(buttons):
    col = cols[i % 2]
    label = item["label"]
    icon = item.get("icon", "")
    if col.button(f"{icon}  {label}", key=f"{current_page}-{label}-{i}"):
        # Append the clicked card to nav_stack
        st.session_state.nav_stack.append(label)
        st.rerun()

