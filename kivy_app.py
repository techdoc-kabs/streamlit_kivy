import streamlit as st
from streamlit_js_eval import streamlit_js_eval
from streamlit_card import card

# -------------------------------
# Card colors for PC cards
# -------------------------------
CARD_COLORS = [
    "linear-gradient(135deg, #1abc9c, #16a085)",
    "linear-gradient(135deg, #3498db, #2980b9)",
    "linear-gradient(135deg, #9b59b6, #8e44ad)",
    "linear-gradient(135deg, #e67e22, #d35400)",
    "linear-gradient(135deg, #e74c3c, #c0392b)",
    "linear-gradient(135deg, #f39c12, #f1c40f)",
]

# -------------------------------
# Detect screen width
# -------------------------------
try:
    width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
except Exception:
    width = None

LARGE_SCREEN_THRESHOLD = 992  # px
use_native_columns = width is not None and width >= LARGE_SCREEN_THRESHOLD

# -------------------------------
# Global CSS for HTML cards (mobile fallback)
# -------------------------------
st.markdown(
    """
    <style>
    .cards-wrap {
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
      justify-content: flex-start;
      padding: 8px 0;
    }
    .card {
      background: #ffffff;
      border-radius: 10px;
      box-shadow: 0 2px 10px rgba(0,0,0,0.06);
      padding: 16px;
      min-width: 160px;
      flex: 0 0 32%;
      box-sizing: border-box;
      transition: transform 0.12s ease;
      overflow: hidden;
      cursor: pointer;
    }
    .card:hover { transform: translateY(-4px); }
    .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
    .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

    @media (max-width: 992px) { .card { flex: 0 0 48%; } }
    @media (max-width: 768px) { .card { flex: 0 0 48%; padding: 12px; min-width: 140px; } }
    @media (max-width: 480px) { .card { flex: 0 0 48%; padding: 10px; min-width: 120px; } }
    @media (max-width: 320px) { .card { flex: 0 0 100%; min-width: 100%; } }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Hybrid Responsive Cards Example")

# -------------------------------
# PC: Streamlit cards
# -------------------------------
def display_card_menu_pc(options, session_key, num_cols=4, next_screen=None):
    cols = st.columns(num_cols, gap='small')
    card_height = "200px"
    font_size_title = "36px"
    font_size_text = "20px"

    for idx, option in enumerate(options):
        color = CARD_COLORS[idx % len(CARD_COLORS)]
        with cols[idx % num_cols]:
            clicked = card(
                title=option.get("title", ""),
                text=option.get("text", ""),
                key=f"{session_key}-{idx}",
                styles={
                    "card": {
                        "width": "100%", "height": card_height,
                        "border-radius": "8px",
                        "background": color,
                        "color": "white",
                        "box-shadow": "0 4px 12px rgba(0,0,0,0.25)",
                        "border": "2px solid #600000",
                        "text-align": "center",
                        "margin": "0px",
                    },
                    "text": {"font-family": "serif", "font-size": font_size_text},
                    "title": {"font-family": "serif", "font-size": font_size_title},
                }
            )
            if clicked:
                st.session_state[session_key] = option.get("text")
                if next_screen:
                    st.session_state.screen = next_screen
                st.session_state["__nav_triggered"] = True
                return True
    return False

# -------------------------------
# Mobile: HTML cards inside container
# -------------------------------
def display_card_menu_mobile(options, session_key):
    cards_html = '<div class="cards-wrap">'
    for idx, option in enumerate(options):
        cards_html += f'''
        <div class="card" onclick="window.alert('Selected: {option.get("text","")}')">
            <h3>{option.get("title","")}</h3>
            <p>{option.get("text","")}</p>
        </div>
        '''
    cards_html += '</div>'
    st.markdown(cards_html, unsafe_allow_html=True)

# -------------------------------
# Example usage
# -------------------------------
options = [
    {"title": "Students", "text": "students"},
    {"title": "Teachers", "text": "teachers"},
    {"title": "Parents", "text": "parents"},
    {"title": "Admins", "text": "admins"},
    {"title": "Counselors", "text": "counselors"},
    {"title": "Staff", "text": "staff"},
]

if use_native_columns:
    st.subheader("PC: Streamlit native cards")
    display_card_menu_pc(options, session_key="selected_role", num_cols=4)
else:
    st.subheader("Mobile: HTML flex cards")
    display_card_menu_mobile(options, session_key="selected_role")

st.write(f"Detected screen width: {width}px")
