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

# -------------------- CSS --------------------
CARD_CSS = """
<style>
.card {
    background-color: #4CAF50;
    color: white;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 18px;
    cursor: pointer;
    transition: transform 0.2s, box-shadow 0.2s;
    margin-bottom: 12px;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0px 5px 15px rgba(0,0,0,0.3);
}
.card-icon {
    font-size: 32px;
    margin-bottom: 8px;
}
</style>
"""
st.markdown(CARD_CSS, unsafe_allow_html=True)

# -------------------- Navigation --------------------
if "nav_stack" not in st.session_state:
    st.session_state.nav_stack = ["main"]

current_page = st.session_state.nav_stack[-1]

# Back button
if len(st.session_state.nav_stack) > 1:
    if st.button("⬅ Back"):
        st.session_state.nav_stack.pop()
        current_page = st.session_state.nav_stack[-1]

st.write(f"### {current_page}")

# -------------------- Display cards --------------------
buttons = MENUS.get(current_page, [])
cols = st.columns(2)  # two columns even on mobile

for i, item in enumerate(buttons):
    col = cols[i % 2]
    label = item["label"]
    icon = item.get("icon", "")
    if col.button(f"{icon}  {label}", key=f"{current_page}-{label}"):
        st.session_state.nav_stack.append(label)
        current_page = label
