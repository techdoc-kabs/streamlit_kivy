import streamlit as st
from streamlit_card import card
import importlib
import traceback
import os, base64

from db_connection import run_query

# ---------------- BACKGROUND ----------------
@st.cache_resource
def load_background(image_path: str):
    if not os.path.exists(image_path):
        st.error(f"Background image '{image_path}' not found")
        return None
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def set_full_page_background(image_path: str):
    encoded = load_background(image_path)
    if encoded:
        st.markdown(f"""
            <style>
            [data-testid="stApp"] {{
                background-image: url("data:image/jpg;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
        """, unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "nav_stack" not in st.session_state:
    st.session_state.nav_stack = ["main"]

# ---------------- SCREEN DETECTION ----------------
def get_screen_width():
    try:
        from streamlit_js_eval import streamlit_js_eval
        width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
    except Exception:
        width = None
    is_mobile = width is not None and width > 703
    return width, is_mobile

# ---------------- PC CARD SETTINGS ----------------
CARD_COLORS = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

def render_pc_cards(cards_list, session_key):
    num_cols = 4
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
                        "box-shadow": "none",
                        "border": "6px solid #600000",
                        "text-align": "center",
                        "margin": "0px",
                    },
                    "title": {"font-family": "serif", "font-size": font_size_title},
                    "text": {"font-family": "serif", "font-size": font_size_text},
                }
            )
            if clicked:
                st.session_state.nav_stack.append(c["text"])  # Use text for navigation
                st.rerun()

# ---------------- MOBILE CARD SETTINGS ----------------
def render_mobile_cards(cards_list):
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
    @media (max-width: 600px){
        .card { flex: 1 1 48%; max-width: 48%; }
    }
    </style>
    """
    st.markdown(CARD_CSS, unsafe_allow_html=True)

    cols = st.columns(2)
    for i, c in enumerate(cards_list):
        col = cols[i % 2]
        label = c.get("title", "")
        text_value = c.get("text", "")
        if col.button(label, key=f"mobile-{label}-{i}"):
            st.session_state.nav_stack.append(text_value)  # Use text for navigation
            st.rerun()

# ---------------- MODULE IMPORT ----------------
@st.cache_resource
def import_module_cached(module_name):
    try:
        return importlib.import_module(module_name)
    except ModuleNotFoundError:
        return None

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
        st.error(f"Module '{module_name}' not found.")
        return

    if hasattr(module, "main") and callable(module.main):
        try:
            module.main()
        except Exception as e:
            st.error(f"Error running module '{module_name}': {e}")
            st.text(traceback.format_exc())
    else:
        st.error(f"Module '{module_name}' does not have a callable main() function.")

# ---------------- CARD NAVIGATION ----------------
def render_card_navigation(cards_list, modules):
    width, is_mobile = get_screen_width()

    # Back button
    if len(st.session_state.nav_stack) > 1:
        if st.button("⬅ Back"):
            st.session_state.nav_stack.pop()
            st.rerun()

    current = st.session_state.nav_stack[-1]
    query = st.query_params.get("nav", None)
    if query:
        st.session_state.nav_stack.append(query[0])
        st.rerun()

    # Find card object helper
    def find_card(cards_list, text_value):
        text_value = text_value.lower()
        for c in cards_list:
            if c.get("text", "").lower() == text_value:
                return c
            if "submenu" in c:
                for sub in c["submenu"]:
                    if sub.get("text", "").lower() == text_value:
                        return sub
        return None

    card_obj = find_card(cards_list, current)
    if not card_obj:
        st.error("Card not found!")
        return

    # Render submenu if exists
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

    # Load module if exists
    if modules.get(parent_page) and modules[parent_page].get(card_obj["text"]):
        module_name = modules[parent_page][card_obj["text"]].get("module")
        if module_name:
            load_module(modules, parent_page, card_obj["text"])
        else:
            st.info(f"Coming soon: {card_obj['text']}")
    else:
        st.info(f"Coming soon: {card_obj['text']}")

# ---------------- MENU DEFINITION ----------------
CARDS = [
    {"title": "🗓️", "text": "Schedules", "submenu": [
        {"title": "📝", "text": "Enroll Clients"},
        {"title": "💢", "text": "Assign Tools"},
        {"title": "⏳", "text": "Status"}
    ]},
    {"title": "📚", "text": "Activity Reports", "submenu": [
        {"title": "💹", "text": "Activities"},
        {"title": "🧠", "text": "Conditions"},
        {"title": "🌍", "text": "Impact"}
    ]},
    {"title": "📈", "text": "Analysis Reports", "submenu": [
        {"title": "📦", "text": "Results"},
        {"title": "📊", "text": "Graphs"}
    ]},
    {"title": "☎️", "text": "Online Calls", "submenu": [
        {"title": "🙋‍♀️", "text": "Need Help"},
        {"title": "💬", "text": "Feedback"},
        {"title": "📅", "text": "Bookings"}
    ]},
    {"title": "🗃️", "text": "Files", "submenu": []},
    {"title": "👨‍👩‍👧‍👦", "text": "Parent Reports", "submenu": []},  
    {"title": "👩‍🏫", "text": "Teacher Reports", "submenu": []},
    {"title": "🗄️", "text": "Resources", "submenu": [
        {"title": "🎥", "text": "Videos"},
        {"title": "🎙️", "text": "Podcasts"},
        {"title": "📖", "text": "Publish"}
    ]}
]

MODULES = {
    "Schedules": {
        "Enroll Clients": {"module": "appointments"},
        "Assign Tools": {"module": "assingn_tools"},
        "Status": {"module": "track_screen_status"},
    },
    "Activity Reports": {
        "Activities": {"module": "activity_summary"},
        "Conditions": {"module": "screen_results_mult"},
        "Impact": {"module": "impact"},
    },
    "Analysis Reports": {
        "Results": {"module": "screen_results_mult"},
        "Graphs": {"module": "graphs"},
    },
    "Online Calls": {
        "Need Help": {"module": "need_help"},
        "Feedback": {"module": "admin_feedback"},
        "Bookings": {"module": "bookings"},
    },
    "Resources": {
        "Videos": {"module": "video_handles"},
        "Podcasts": {"module": None},
        "Publish": {"module": None},
    },
    "Files": {
        "Files": {"module": "entire_file"}
    },
    "Teacher Reports": {
        "Teacher Reports": {"module": "teacher_reports"}
    },
    "Parent Reports": {
        "Parent Reports": {"module": "entire_file"}
    }
}

# ---------------- MAIN ----------------
def main():
    render_card_navigation(CARDS, MODULES)

if __name__ == "__main__":
    main()
