import streamlit as st
from streamlit_card import card
from streamlit_js_eval import streamlit_js_eval

# -------------------------------
# Demo cards
# -------------------------------
cards = [
    {"title": "Reports", "body": "Summary of recent reports.", "submenu": ["Financial", "Activity"]},
    {"title": "Analytics", "body": "Interactive charts.", "submenu": []},
    {"title": "Archives", "body": "Browse archived documents.", "submenu": []},
    {"title": "Team", "body": "Quick team stats.", "submenu": []}
]

# -------------------------------
# Navigation state
# -------------------------------
if "nav_stack" not in st.session_state:
    st.session_state.nav_stack = []

# -------------------------------
# Device detection
# -------------------------------
try:
    width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
except Exception:
    width = 1024
is_pc = width >= 992

# -------------------------------
# CSS for mobile cards
# -------------------------------
st.markdown("""
<style>
.cards-wrap { display:flex; gap:12px; flex-wrap:wrap; padding:8px 0; justify-content:flex-start; }
.card { background:#fff; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.06);
        padding:16px; min-width:160px; flex:0 0 32%; transition: transform 0.12s ease;
        overflow:hidden; cursor:pointer; }
.card:hover { transform: translateY(-4px); }
.card h3 { margin:6px 0; font-size:clamp(16px,1.6vw,20px); }
.card p { margin:4px 0; font-size:clamp(13px,1.1vw,15px); color:#333; }
@media (max-width:992px){ .card{ flex:0 0 48%; } }
@media (max-width:480px){ .cards-wrap{ justify-content: space-around; } .card{ flex:0 0 48%; padding:14px; min-width:140px;} }
@media (max-width:350px){ .card{ flex:0 0 48%; min-width:100%; } }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# Find card by title
# -------------------------------
def find_card(title):
    for c in cards:
        if c["title"].lower() == title:
            return c
        if "submenu" in c and title in [s.lower() for s in c["submenu"]]:
            return {"title": title, "body": f"{title.title()} report.", "submenu": []}
    return None

# -------------------------------
# PC rendering (streamlit-card)
# -------------------------------
def display_cards_pc(cards_list):
    cols = st.columns(4, gap ='small')
    for idx, c in enumerate(cards_list):
        with cols[idx % 4]:
            clicked = card(
                title=c["title"],
                text=c.get("body", ""),
                key=f"pc-card-{c['title']}"
            )
            if clicked:
                st.session_state.nav_stack.append(c["title"].lower())
                st.rerun()

# -------------------------------
# Mobile rendering (HTML + JS)
def display_cards_mobile(cards_list):
    html = '<div class="cards-wrap">'
    for i, c in enumerate(cards_list):
        html += f'''<div class="card" onclick="window.parent.postMessage({{
            isStreamlitMessage: true,
            type: 'streamlit:setComponentValue',
            value: '{c["title"].lower()}'
        }}, '*')">
            <h3>{c["title"]}</h3>
            <p>{c.get("body","")}</p>
        </div>
        '''
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)

    # Here we just listen for the result (no big JS block)
    result = streamlit_js_eval(js_expressions="", key="MOBILE_CARD_CLICK", label="mobile-card-click")
    if result:
        st.session_state.nav_stack.append(result)
        st.rerun()
# -------------------------------
# Render current level
# -------------------------------
current_level = st.session_state.nav_stack[-1] if st.session_state.nav_stack else None

if not current_level:
    st.title("Main Menu")
    if is_pc:
        display_cards_pc(cards)
    else:
        display_cards_mobile(cards)
else:
    card_obj = find_card(current_level)

    if card_obj.get("submenu"):
        st.title(f"{card_obj['title']} Submenu")
        submenu_cards = [{"title": s, "body": f"{s} report."} for s in card_obj["submenu"]]
        if is_pc:
            display_cards_pc(submenu_cards)
        else:
            display_cards_mobile(submenu_cards)
    else:
        st.title(f"{card_obj['title']} Page")
        if card_obj["title"].lower() == "activity":
            st.success("Here you could load cont.main() or another page.")
        else:
            st.write(f"This is the detailed view for **{card_obj['title']}**.")

    # Back button
    if st.button("⬅ Back"):
        st.session_state.nav_stack.pop()
        st.rerun()

st.caption(f"📏 Screen width: {width}px | Current level: {current_level}")

