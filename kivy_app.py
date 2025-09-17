import streamlit as st
from streamlit_card import card
from streamlit_js_eval import streamlit_js_eval

# ---------- Detect screen width ----------
try:
    width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
except Exception:
    width = None

is_mobile = width is not None and width < 768

# ---------- Example card data ----------
cards = [
    {"title": "Reports", "body": "Summary of recent reports.", "submenu": ["Financial", "Activity"]},
    {"title": "Analytics", "body": "Interactive charts.", "submenu": []},
    {"title": "Archives", "body": "Browse archived documents.", "submenu": []},
    {"title": "Team", "body": "Quick team stats.", "submenu": []},
]

# ---------- Session state ----------
if "nav_stack" not in st.session_state:
    st.session_state.nav_stack = []

current_level = st.session_state.nav_stack[-1] if st.session_state.nav_stack else None

# ---------- CSS for HTML cards (mobile) ----------
st.markdown("""
<style>
.cards-wrap {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    padding: 8px 0;
    justify-content: flex-start;
}
.card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.06);
    padding: 16px;
    min-width: 140px;
    flex: 0 0 48%;
    transition: transform 0.12s ease;
    cursor: pointer;
}
.card:hover { transform: translateY(-4px); }
.card h3 { margin: 6px 0; font-size: 16px; }
.card p { margin: 4px 0; font-size: 14px; color: #333; }

@media (min-width: 992px) { .card { flex: 0 0 23%; } } /* 4 cols desktop */
</style>
""", unsafe_allow_html=True)


# ---------- HTML renderer for mobile ----------
def render_mobile_cards(cards_list):
    html = '<div class="cards-wrap">'
    for c in cards_list:
        html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit;">
            <div class="card">
                <h3>{c["title"]}</h3>
                <p>{c.get("body","")}</p>
            </div>
        </a>
        '''
    html += "</div>"
    st.markdown(html, unsafe_allow_html=True)


# ---------- Find card helper ----------
def find_card(title):
    for c in cards:
        if c["title"].lower() == title:
            return c
        if "submenu" in c and title in [s.lower() for s in c["submenu"]]:
            return {"title": title, "body": f"{title.title()} report.", "submenu": []}
    return None


# ---------- Navigation ----------
query_params = st.query_params
clicked = query_params.get("nav", None)

if clicked:
    st.session_state.nav_stack.append(clicked)
    # clear query param
    st.query_params.clear()
    st.rerun()


# ---------- Rendering ----------
if not current_level:
    st.title("Main Menu")

    if is_mobile:
        render_mobile_cards(cards)
    else:
        cols = st.columns(4)
        for i, c in enumerate(cards):
            with cols[i % 4]:
                if card(
                    title=c["title"],
                    text=c.get("body", ""),
                    key=f"pc-{c['title']}"
                ):
                    st.session_state.nav_stack.append(c["title"].lower())
                    st.rerun()

else:
    card_obj = find_card(current_level)

    if card_obj.get("submenu"):
        st.title(f"{card_obj['title']} Submenu")
        sub_cards = [{"title": s, "body": f"{s} report."} for s in card_obj["submenu"]]
        if is_mobile:
            render_mobile_cards(sub_cards)
        else:
            cols = st.columns(4)
            for i, c in enumerate(sub_cards):
                with cols[i % 4]:
                    if card(title=c["title"], text=c["body"], key=f"pc-{c['title']}"):
                        st.session_state.nav_stack.append(c["title"].lower())
                        st.rerun()
    else:
        st.title(f"{card_obj['title']} Page")
        st.write(f"This is the detailed view for **{card_obj['title']}**.")

    if st.button("⬅ Back"):
        st.session_state.nav_stack.pop()
        st.rerun()
