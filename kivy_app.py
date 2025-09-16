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
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 8px;
    }
    @media (max-width: 350px) {
        .product-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }
    .product-card {
        background: #fff;
        border: 1px solid #ddd;
        border-radius: 10px;
        text-align: center;
        padding: 10px;
        font-family: Arial;
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
    .add-to-cart {
        display: inline-block;
        margin-top: 6px;
        background: #f39c12;
        color: white;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 13px;
        cursor: pointer;
        text-decoration: none;
    }
    .add-to-cart:hover {
        background: #e67e22;
    }
    </style>
""", unsafe_allow_html=True)

# --- Render products ---
html = '<div class="product-grid">'
for i, p in enumerate(products):
    html += f"""<div class="product-card">
        <img src="{p['img']}" alt="{p['name']}">
        <div class="product-name">{p['name']}</div>
        <div class="product-price">{p['price']} <span class="discount">-{p['discount']}</span></div>
        <a class="add-to-cart" href="?add={i}">🛒 Add to Cart</a>
    </div>
    """
html += "</div>"

st.markdown(html, unsafe_allow_html=True)

# --- Handle Add to Cart ---
query_params = st.query_params
if "add" in query_params:
    idx = int(query_params["add"])
    if products[idx] not in st.session_state.cart:
        st.session_state.cart.append(products[idx])
        st.success(f"✅ {products[idx]['name']} added to cart!")

# --- Cart Preview ---
st.markdown("### 🛍️ Your Cart")
if st.session_state.cart:
    for item in st.session_state.cart:
        st.write(f"- {item['name']} ({item['price']})")
else:
    st.info("Your cart is empty.")





