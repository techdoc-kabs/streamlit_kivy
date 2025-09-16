import streamlit as st
from streamlit_card import card

# ---------------- Detect mobile (or small screen) ----------------
from streamlit_javascript import st_javascript
screen_width = st_javascript("window.innerWidth", key="screen_width") or 1024
is_mobile = screen_width < 704  # treat <704px as mobile/small screen

# Example card colors
CARD_COLORS = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c", "#e67e22", "#34495e"]

def display_card_menu(options: list, session_key: str, next_screen=None):
    # Determine number of columns based on screen width
    if screen_width >= 704:
        num_cols = 4
    elif screen_width >= 320:
        num_cols = 3
    else:
        num_cols = 2

    cols = st.columns(num_cols, gap='small')
    card_height = "150px" if is_mobile else "200px"
    font_size_title = "40px" if is_mobile else "60px"
    font_size_text = "20px" if is_mobile else "25px"

    for idx, option in enumerate(options):
        color = CARD_COLORS[idx % len(CARD_COLORS)]
        col = cols[idx % num_cols]  # assign card to a column
        with col:
            clicked = card(
                title=option.get("title", ""),
                text=option.get("text", ""),
                key=f"{session_key}-{option.get('text','')}",
                styles={
                    "card": {
                        "width": "100%", "height": card_height,
                        "border-radius": "8px",
                        "background": color,
                        "color": "white",
                        "box-shadow": "0 4px 12px rgba(0,0,0,0.25)",
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

# ---------------- Example Usage ----------------
st.title("Responsive Card Menu Example")

cards = [
    {"title": "🗓️", "text": "Schedules"},
    {"title": "📚", "text": "Reports"},
    {"title": "📈", "text": "Analysis"},
    {"title": "📧", "text": "Messages"},
    {"title": "🗃️", "text": "Files"},
    {"title": "🗄️", "text": "Resources"},
    {"title": "⚙️", "text": "Settings"},
    {"title": "🔔", "text": "Notifications"},
]

clicked = display_card_menu(cards, session_key="selected_page")
if clicked:
    st.success(f"You clicked: {st.session_state['selected_page']}")
