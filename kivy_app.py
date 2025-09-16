# import streamlit as st
# from streamlit_card import card

# # ---------------- Detect mobile (or small screen) ----------------
# from streamlit_javascript import st_javascript
# screen_width = st_javascript("window.innerWidth", key="screen_width") or 1024
# is_mobile = screen_width < 704  # treat <704px as mobile/small screen

# # Example card colors
# CARD_COLORS = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6", "#1abc9c", "#e67e22", "#34495e"]

# def display_card_menu(options: list, session_key: str, next_screen=None):
#     # Determine number of columns based on screen width
#     if screen_width >= 704:
#         num_cols = 4
#     elif screen_width >= 320:
#         num_cols = 3
#     else:
#         num_cols = 2

#     cols = st.columns(num_cols, gap='small')
#     card_height = "150px" if is_mobile else "200px"
#     font_size_title = "40px" if is_mobile else "60px"
#     font_size_text = "20px" if is_mobile else "25px"

#     for idx, option in enumerate(options):
#         color = CARD_COLORS[idx % len(CARD_COLORS)]
#         col = cols[idx % num_cols]  # assign card to a column
#         with col:
#             clicked = card(
#                 title=option.get("title", ""),
#                 text=option.get("text", ""),
#                 key=f"{session_key}-{option.get('text','')}",
#                 styles={
#                     "card": {
#                         "width": "100%", "height": card_height,
#                         "border-radius": "8px",
#                         "background": color,
#                         "color": "white",
#                         "box-shadow": "0 4px 12px rgba(0,0,0,0.25)",
#                         "text-align": "center",
#                         "margin": "0px",
#                     },
#                     "text": {"font-family": "serif", "font-size": font_size_text},
#                     "title": {"font-family": "serif", "font-size": font_size_title},
#                 }
#             )
#             if clicked:
#                 st.session_state[session_key] = option.get("text")
#                 if next_screen:
#                     st.session_state.screen = next_screen
#                 st.session_state["__nav_triggered"] = True
#                 return True
#     return False

# # ---------------- Example Usage ----------------
# st.title("Responsive Card Menu Example")

# cards = [
#     {"title": "🗓️", "text": "Schedules"},
#     {"title": "📚", "text": "Reports"},
#     {"title": "📈", "text": "Analysis"},
#     {"title": "📧", "text": "Messages"},
#     {"title": "🗃️", "text": "Files"},
#     {"title": "🗄️", "text": "Resources"},
#     {"title": "⚙️", "text": "Settings"},
#     {"title": "🔔", "text": "Notifications"},
# ]

# clicked = display_card_menu(cards, session_key="selected_page")
# if clicked:
#     st.success(f"You clicked: {st.session_state['selected_page']}")

# import streamlit as st

# # Example cards
# cards = [
#     {"title": "🗓️", "text": "Schedules"},
#     {"title": "📚", "text": "Reports"},
#     {"title": "📈", "text": "Analysis"},
#     {"title": "📧", "text": "Messages"},
#     {"title": "🗃️", "text": "Files"},
#     {"title": "🗄️", "text": "Resources"},
# ]

# # ---------------- Responsive CSS wrapper ----------------
# st.markdown("""
# <style>
# .cards-wrap {
#     display: flex;
#     flex-wrap: wrap;
#     gap: 8px;
#     margin: 0;
#     padding: 0;
#     box-sizing: border-box;
# }
# .card {
#     flex: 0 0 calc(25% - 8px);  /* default 4 columns for large screens */
#     min-width: 120px;
#     background: #3498db;
#     color: white;
#     height: 150px;
#     display: flex;
#     flex-direction: column;
#     align-items: center;
#     justify-content: center;
#     border-radius: 8px;
#     text-align: center;
#     box-shadow: 0 4px 12px rgba(0,0,0,0.25);
# }

# /* Medium screens: 3 columns */
# @media (max-width: 704px) {
#     .card {
#         flex: 0 0 calc(33.33% - 8px);
#     }
# }

# /* Small screens (mobile): 2 columns */
# @media (max-width: 320px) {
#     .card {
#         flex: 0 0 calc(50% - 6px);
#     }
# }

# .card h3 {
#     font-size: 1.5em;
#     margin: 4px 0;
# }
# .card p {
#     font-size: 1em;
#     margin: 0;
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------------- Render cards in HTML wrapper ----------------
# cards_html = '<div class="cards-wrap">'
# for c in cards:
#     cards_html += f'''<div class="card">
#         <h3>{c["title"]}</h3>
#         <p>{c["text"]}</p>
#     </div>
#     '''
# cards_html += '</div>'

# st.markdown(cards_html, unsafe_allow_html=True)

import streamlit as st

# --- JavaScript to detect screen width ---
screen_width = st.session_state.get("screen_width", None)
get_width_script = """
<script>
    const width = window.innerWidth;
    var streamlitDoc = window.parent.document;
    var input = streamlitDoc.querySelector('input#screen-width');
    if (!input) {
        input = streamlitDoc.createElement('input');
        input.id = 'screen-width';
        input.type = 'hidden';
        input.value = width;
        streamlitDoc.body.appendChild(input);
        input.dispatchEvent(new Event('change'));
    } else {
        input.value = width;
        input.dispatchEvent(new Event('change'));
    }
</script>
"""
st.markdown(get_width_script, unsafe_allow_html=True)

# Hidden input to capture JS value
screen_width = st.text_input("Screen Width", key="screen-width", label_visibility="collapsed")

# --- Decide number of columns based on width ---
try:
    width = int(screen_width)
    num_cols = 2 if width <= 350 else 4
except:
    num_cols = 4  # default if width not detected

# --- Products ---
products = [
    {"name": "iGG Black", "price": "UGX 500,000", "img": "https://via.placeholder.com/150"},
    {"name": "iGG RAM 256GB SSD", "price": "UGX 1,200,000", "img": "https://via.placeholder.com/150"},
    {"name": "Nice Chandelier", "price": "UGX 260,000", "img": "https://via.placeholder.com/150"},
    {"name": "Bluetooth Device", "price": "UGX 150,000", "img": "https://via.placeholder.com/150"},
]

if "cart" not in st.session_state:
    st.session_state.cart = []

def add_to_cart(product):
    st.session_state.cart.append(product)
    st.toast(f"✅ {product['name']} added to cart!")

# --- Custom CSS for product cards ---
st.markdown("""
    <style>
    .product-card {
        background: #fff;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        padding: 15px;
        text-align: center;
        margin: 10px;
    }
    .product-card img {
        width: 100%;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .product-name {
        font-weight: 600;
        font-size: 16px;
        margin-bottom: 5px;
    }
    .product-price {
        color: #e67e22;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .stButton button {
        width: 100%;
        background: #f39c12;
        color: white;
        border-radius: 8px;
        font-weight: bold;
    }
    .stButton button:hover {
        background: #e67e22;
    }
    </style>
""", unsafe_allow_html=True)

# --- Display products in responsive columns ---
cols = st.columns(num_cols)

for i, product in enumerate(products):
    with cols[i % num_cols]:
        st.markdown(
            f"""
            <div class="product-card">
                <img src="{product['img']}" alt="{product['name']}">
                <div class="product-name">{product['name']}</div>
                <div class="product-price">{product['price']}</div>
            </div>
            """, unsafe_allow_html=True
        )
        if st.button("🛒 Add to Cart", key=f"cart_{i}"):
            add_to_cart(product)

# --- Cart preview ---
st.markdown("### 🛍️ Your Cart")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"- {item['name']} ({item['price']})")
else:
    st.info("Your cart is empty.")
