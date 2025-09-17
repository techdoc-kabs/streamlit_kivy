
import streamlit as st
from streamlit_card import card
from streamlit_js_eval import streamlit_js_eval
import importlib
import traceback

if "nav_stack" not in st.session_state:
    st.session_state.nav_stack = []
try:
    width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
except Exception:
    width = None


is_mobile = width is not None and width <  1200

CARD_COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]


@st.cache_data
def get_cards_css():
    return """
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
    """
st.markdown(get_cards_css(), unsafe_allow_html=True)

# ---------- Sanitize cards ----------
def sanitize_cards(cards_list):
    sanitized = []
    for c in cards_list:
        new_c = {
            "title": str(c.get("title","")),
            "text": str(c.get("text","")),
            "submenu": sanitize_cards(c.get("submenu",[])) if "submenu" in c else []}
        sanitized.append(new_c)
    return sanitized

# ---------- Find card helper ----------
def find_card(cards_list, title):
    title = title.lower()
    for c in cards_list:
        # Check main card
        if c["text"].lower() == title:
            return c
        # Check submenu cards
        if "submenu" in c:
            for sub in c["submenu"]:
                if sub["text"].lower() == title:
                    return sub
    return None

# ---------- Mobile cards ----------
@st.cache_data
def build_mobile_cards_html(cards_list):
    cards_list = sanitize_cards(cards_list)
    html = '<div class="cards-wrap">'
    for c in cards_list:
        html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit;">
            <div class="card">
                <h3>{c["title"]}</h3>
                <p>{c.get("text","")}</p>
            </div>
        </a>
        '''
    html += "</div>"
    return html

def render_mobile_cards(cards_list):
    html = build_mobile_cards_html(cards_list)
    st.markdown(html, unsafe_allow_html=True)

# ---------- PC card renderer ----------
def render_pc_cards(cards_list, session_key):
    num_cols = 3
    cols = st.columns(num_cols, gap='small')
    card_height = "180px"
    font_size_title = "60px"
    font_size_text = "20px"

    for idx, c in enumerate(cards_list):
        color = CARD_COLORS[idx % len(CARD_COLORS)]
        with cols[idx % num_cols]:
            clicked = card(
                title=c.get("title", ""),
                text=c.get("text", ""),
                key=f"{session_key}-{c.get('title','')}",
                styles={
                    "card": {
                        "width": "100%",
                        "height": card_height,
                        "border-radius": "0px",
                        "background": color,
                        "color": "white",
                        "box-shadow": "0 4px 12px rgba(0,0,0,0.25)",
                        "border": "2px solid #600000",
                        "text-align": "center",
                        "margin": "0px",
                    },
                    "title": {"font-family": "serif", "font-size": font_size_title},
                    "text": {"font-family": "serif", "font-size": font_size_text},
                }
            )
            if clicked:
                st.session_state.nav_stack.append(c["text"].lower())
                st.rerun()

@st.cache_resource
def import_module_cached(module_name):
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        return None

# ---------- Load module ----------
def load_module(modules, page_text, sub_text=None):
    page_modules = modules.get(page_text, {})
    target_key = sub_text if sub_text else page_text
    module_info = page_modules.get(target_key)

    if not module_info:
        st.info(f"Coming Soon: {target_key}")
        return

    module_name = module_info.get("module")
    if not module_name:
        st.info(f"Module not available yet for {target_key}")
        return

    module = import_module_cached(module_name)
    if not module:
        st.error(f"Module '{module_name}' not found. Create '{module_name}.py'.")
        return

    if hasattr(module, "main") and callable(module.main):
        try:
            module.main()
        except Exception as e:
            st.error(f"Error running module '{module_name}': {e}")
            st.text(traceback.format_exc())
    else:
        st.error(f"Module '{module_name}' does not have a callable main() function.")




def render_card_navigation(cards_list, modules):
    if st.session_state.nav_stack:
        if st.button("⬅ Back"):
            st.session_state.nav_stack.pop()
            st.rerun()
    current = st.session_state.nav_stack[-1] if st.session_state.nav_stack else None
    query = st.query_params.get("nav", None)
    if query:
        st.session_state.nav_stack.append(query[0])
        st.rerun()
    if not current:
        if is_mobile:
            render_mobile_cards(cards_list)
        else:
            render_pc_cards(cards_list, "main")
        return
    card_obj = find_card(cards_list, current)
    if not card_obj:
        st.error("Card not found!")
        return
    if "submenu" in card_obj and card_obj["submenu"]:
        if is_mobile:
            render_mobile_cards(card_obj["submenu"])
        else:
            render_pc_cards(card_obj["submenu"], f"submenu-{card_obj['text']}")
        return
    parent_page = None
    for c in cards_list:
        if "submenu" in c and card_obj in c["submenu"]:
            parent_page = c["text"]
            break
    parent_page = parent_page or card_obj["text"]

    if modules.get(parent_page) and modules[parent_page].get(card_obj["text"]):
        module_name = modules[parent_page][card_obj["text"]].get("module")
        if module_name:
            load_module(modules, parent_page, card_obj["text"])
        else:
            st.info(f"Coming soon: {card_obj['text']}")
    else:
        st.info(f"Coming soon: {card_obj['text']}")


MODULES = {
    "Schedules": {
        "Enroll Clients": {"module": "appointments"},
        "Assign Tools": {"module": "assingn_tools"},
        "Status": {"module": "track_screen_status"},
    },
    "Reports": {
        "Activities": {"module": "activity_summary"},
        "Conditions": {"module": "screen_results_mult"},
        "Impact": {"module": "impact"},
    },
    "Analysis": {
        "Results": {"module": "screen_results_mult"},
        "Graphs": {"module": "graphs"},
    },
    "Messages": {
        "Need help": {"module": "need_help"},
        "Feedback": {"module": "feedback"},
        "Bookings": {"module": "bookings"},
    },
    "Resources": {
        "Videos": {"module": "video_handles"},
        "Podcasts": {"module": None},
        "Publish": {"module": None},
    },
    "Files": {
        "Files": {"module": "entire_file"}
    }
}


# ---------- MENU DEFINITION ----------
CARDS = [
    {"title": "🗓️", "text": "Schedules", "submenu": [
        {"title": "📝", "text": "Enroll Clients"},
        {"title": "💢", "text": "Assign Tools"},
        {"title": "⏳", "text": "Status"}
    ]},
    {"title": "📚", "text": "Reports", "submenu": [
        {"title": "💹", "text": "Activities"},
        {"title": "🧠", "text": "Conditions"},
        {"title": "🌍", "text": "Impact"}
    ]},
    {"title": "📈", "text": "Analysis", "submenu": [
        {"title": "📦", "text": "Results"},
        {"title": "📊", "text": "Graphs"}
    ]},
    {"title": "📧", "text": "Messages", "submenu": [
        {"title": "🙋‍♀️", "text": "Need Help"},
        {"title": "💬", "text": "Feedback"},
        {"title": "📅", "text": "Bookings"}
    ]},
    {"title": "🗃️", "text": "Files", "submenu": []},  # no submenu, direct
    {"title": "🗄️", "text": "Resources", "submenu": [
        {"title": "🎥", "text": "Videos"},
        {"title": "🎙️", "text": "Podcasts"},
        {"title": "📖", "text": "Publish"}
    ]}
]

def main():
    defaults = {
        "user_info": {}}
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    # set_full_page_background('images/psy4.jpg')
    # ------------------ USER ------------------
    username = st.session_state.get("user_info", {}).get("username", "guest")
    render_card_navigation(CARDS, MODULES)
if __name__ == "__main__":
    main()
