import streamlit as st
from streamlit_javascript import st_javascript

# -------------------------------
# Device detection
# -------------------------------
def get_device_type(width):
    try:
        w = int(width)
    except (ValueError, TypeError):
        return "desktop"
    return "mobile" if w < 704 else "desktop"

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
# Responsive card menu function using a flex container
# -------------------------------
def display_card_menu_html(options: list, session_key: str, next_screen=None):
    """
    Display a responsive card menu using CSS flex/grid.
    Ensures multi-column layout even on mobile.
    """
    card_height = "150px" if is_mobile else "200px"
    font_size_title = "20px" if is_mobile else "36px"
    font_size_text = "12px" if is_mobile else "18px"

    # Determine number of columns based on device
    if is_mobile:
        columns = 2  # always 2 columns on mobile
    else:
        columns = 4  # desktop

    # Start the flex container
    cards_html = f'<div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center;">'

    for idx, option in enumerate(options):
        color = CARD_COLORS[idx % len(CARD_COLORS)]
        cards_html += f'''<div style="
            flex: 1 1 calc({100/columns}% - 10px);
            max-width: calc({100/columns}% - 10px);
            height: {card_height};
            border-radius: 12px;
            background: {color};
            color: white;
            box-shadow: 0 4px 12px rgba(0,0,0,0.25);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            cursor:pointer;
            margin-bottom:10px;
        " onclick="window.location.href='#'">
            <h3 style='margin:5px; font-size:{font_size_title};'>{option.get("title","")}</h3>
            <p style='margin:5px; font-size:{font_size_text};'>{option.get("text","")}</p>
        </div>
        '''

    cards_html += '</div>'

    st.markdown(cards_html, unsafe_allow_html=True)

# -------------------------------
# Example usage
# -------------------------------
st.title("Responsive Card Menu (Flex Container)")

options = [
    {"title": "Students", "text": "students"},
    {"title": "Teachers", "text": "teachers"},
    {"title": "Parents", "text": "parents"},
    {"title": "Admins", "text": "admins"},
    {"title": "Counselors", "text": "counselors"},
    {"title": "Staff", "text": "staff"},
]

display_card_menu_html(options, session_key="selected_role")

st.write(f"Device width: {device_width}px, Detected: {device_type}")

