import streamlit as st

# --- Products ---
products = [
    {"name": "Chiq 43 Inch Smart TV", "price": "UGX 657,000", "discount": "34%", "img": "https://via.placeholder.com/200"},
    {"name": "Samsung Galaxy A05", "price": "UGX 274,900", "discount": "54%", "img": "https://via.placeholder.com/200"},
    {"name": "iGG RAM 256GB SSD", "price": "UGX 1,200,000", "discount": "45%", "img": "https://via.placeholder.com/200"},
    {"name": "Nice Chandelier", "price": "UGX 260,000", "discount": "31%", "img": "https://via.placeholder.com/200"},
    {"name": "Bluetooth Device", "price": "UGX 150,000", "discount": "20%", "img": "https://via.placeholder.com/200"},
    {"name": "Smart Watch", "price": "UGX 320,000", "discount": "15%", "img": "https://via.placeholder.com/200"},
    {"name": "Wireless Earbuds", "price": "UGX 180,000", "discount": "25%", "img": "https://via.placeholder.com/200"},
    {"name": "Portable Speaker", "price": "UGX 210,000", "discount": "18%", "img": "https://via.placeholder.com/200"},
]

if "cart" not in st.session_state:
    st.session_state.cart = []

# --- Custom CSS Grid ---
st.markdown("""
    <style>
    .product-grid {
        display: grid !important;
        grid-template-columns: repeat(4, 1fr) !important;
        gap: 10px !important;
    }
    @media only screen and (max-width: 350px) {
        .product-grid {
            grid-template-columns: repeat(2, 1fr) !important;
        }
    }
    .product-card {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        text-align: center;
        padding: 10px;
        font-family: Arial, sans-serif;
    }
    .product-card img {
        width: 100%;
        border-radius: 8px;
        margin-bottom: 8px;
    }
    .product-name {
        font-weight: bold;
        font-size: 14px;
        margin-bottom: 5px;
    }
    .product-price {
        color: #e67e22;
        font-weight: bold;
        font-size: 13px;
        margin-bottom: 5px;
    }
    .discount {
        background: #ff4d4d;
        color: white;
        font-size: 11px;
        padding: 2px 5px;
        border-radius: 4px;
    }
    .stButton button {
        width: 100%;
        background: #f39c12;
        color: white;
        border-radius: 6px;
        font-size: 13px;
        font-weight: bold;
    }
    .stButton button:hover {
        background: #e67e22;
    }
    </style>
""", unsafe_allow_html=True)

# --- Render Products in Grid ---
cols_html = '<div class="product-grid">'
for i, p in enumerate(products):
    cols_html += f"""
    <div class="product-card">
        <img src="{p['img']}" alt="{p['name']}">
        <div class="product-name">{p['name']}</div>
        <div class="product-price">{p['price']} <span class="discount">-{p['discount']}</span></div>
        <div id="btn{i}"></div>
    </div>
    """
cols_html += "</div>"

# Inject HTML skeleton
st.markdown(cols_html, unsafe_allow_html=True)

# Inject buttons into product cards
for i, p in enumerate(products):
    with st.container():
        button_ph = st.empty()
        with button_ph:
            if st.button(f"🛒 Add to Cart", key=f"cart_{i}"):
                st.session_state.cart.append(p)
                st.success(f"✅ {p['name']} added to cart!")
