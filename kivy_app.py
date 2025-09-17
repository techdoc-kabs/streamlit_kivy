import streamlit as st
from streamlit_javascript import st_javascript
from streamlit_card import card

# -------------------------------
# Device detection
# -------------------------------
def get_device_type(width):
    """Detect device type based on screen width"""
    try:
        w = int(width)
    except (ValueError, TypeError):
        return "desktop"
    return "mobile" if w < 704 else "desktop"

# Get screen width from frontend
device_width = st_javascript("window.innerWidth", key="screen_width") or 1024
device_type = get_device_type(device_width)
is_mobile = device_type == "mobile"

# -------------------------------
# Card gradient colors
# -------------------------------
CARD_COLORS = [
    "linear-gradient(135deg, #1abc9c, #16a085)",
    "linear-gradient(135deg, #3498db, #2980b9)",
    "linear-gradient(135deg, #9b59b6, #8e44ad)",
    "linear-gradient(135deg, #e67e22, #d35400)",
    "linear-gradient(135deg, #e74c3c, #c0392b)",
    "linear-gradient(135deg, #f39c12, #f1c40f)",
    "linear-gradient(135deg, #2ecc71, #27ae60)",
    "linear-gradient(135deg, #34495e, #2c3e50)",
]

# -------------------------------
# Responsive card menu function
# -------------------------------
def display_card_menu(options: list, session_key: str, max_cols_desktop: int = 4, next_screen=None):
    """
    Display a responsive card menu.

    - options: list of dicts with keys 'title' and 'text'
    - session_key: key to store clicked value in st.session_state
    - max_cols_desktop: max columns on desktop
    - next_screen: optional next screen to trigger
    """
    # Determine number of columns dynamically
    if is_mobile:
        # Force at least 2 columns even on narrow phones
        cols_count = min(3, max(2, device_width // 150))  # 150px per card minimum
    else:
        cols_count = max_cols_desktop

    cols = st.columns(cols_count, gap="small")

    # Card styling based on device
    card_height = "150px" if is_mobile else "200px"
    font_size_title = "24px" if is_mobile else "36px"
    font_size_text = "14px" if is_mobile else "20px"

    for idx, option in enumerate(options):
        color = CARD_COLORS[idx % len(CARD_COLORS)]
        col_idx = idx % cols_count
        with cols[col_idx]:
            clicked = card(
                title=option.get("title", ""),
                text=option.get("text", ""),
                key=f"{session_key}-{idx}",
                styles={
                    "card": {
                        "width": "100%",
                        "height": card_height,
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
                    st.session_state["screen"] = next_screen
                st.session_state["__nav_triggered"] = True
                return True
    return False

# -------------------------------
# Example usage
# -------------------------------
st.title("Responsive Card Menu Demo")

options = [
    {"title": "Students", "text": "students"},
    {"title": "Teachers", "text": "teachers"},
    {"title": "Parents", "text": "parents"},
    {"title": "Admins", "text": "admins"},
    {"title": "Counselors", "text": "counselors"},
    {"title": "Staff", "text": "staff"},
]

clicked = display_card_menu(options, session_key="selected_role", next_screen="dashboard")

if "selected_role" in st.session_state:
    st.success(f"Selected Role: {st.session_state['selected_role']}")
