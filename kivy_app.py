import streamlit as st

# Define the card menus
MENUS = {
    "main": [
        {"title": "Consultations"},
        {"title": "Reports"},
        {"title": "Files"},
        {"title": "Schedules"},
    ],
    "Consultations": [
        {"title": "New Session"},
        {"title": "History"},
    ],
    "Schedules": [
        {"title": "Upcoming"},
        {"title": "Past"},
    ],
}

# Get current page from query params
params = st.query_params
current_page = params.get("page", "main")

# Back Button
if current_page != "main":
    if st.button("⬅ Back", use_container_width=True):
        # Find parent page
        for parent, submenu in MENUS.items():
            if any(item["title"] == current_page for item in submenu):
                st.query_params["page"] = parent
                st.rerun()
        st.query_params["page"] = "main"
        st.rerun()

# CSS for HTML-like clickable cards
st.markdown("""
<style>
.cards-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: center;
}
.card-btn {
    background: #2ecc71;
    color: white;
    border-radius: 12px;
    padding: 16px;
    flex: 0 0 48%;
    max-width: 260px;
    cursor: pointer;
    text-align: center;
    transition: transform 0.2s;
    border: none;
}
.card-btn:hover { transform: translateY(-5px); background: #27ae60; }
@media (min-width: 992px) {
    .card-btn { flex: 0 0 23%; }
}
</style>
""", unsafe_allow_html=True)

# Render Cards
cols_per_row = 2
cards = MENUS.get(current_page, [])

st.write(f"### {current_page}")

for i in range(0, len(cards), cols_per_row):
    cols = st.columns(cols_per_row)
    for col, card in zip(cols, cards[i:i+cols_per_row]):
        if col.button(card["title"], key=card["title"], help=f"Open {card['title']}", use_container_width=True):
            st.query_params["page"] = card["title"]
            st.rerun()
