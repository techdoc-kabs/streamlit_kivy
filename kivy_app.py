import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
        /* Default Streamlit columns behave normally on desktop */

        /* Phones: force 2 columns side by side */
        @media (max-width: 768px) {
            [data-testid="stHorizontalBlock"] {
                flex-wrap: wrap !important;
                flex-direction: row !important;
                justify-content: space-between;
            }
            [data-testid="column"] {
                min-width: 48% !important;   /* 2 columns per row */
                flex: 1 1 48% !important;
            }
        }

        /* Very small phones like 320px */
        @media (max-width: 320px) {
            [data-testid="column"] {
                min-width: 100% !important;  /* fallback to single column */
                flex: 1 1 100% !important;
            }
        }

        /* Card styling */
        .card {
            background: #f9f9f9;
            border-radius: 12px;
            padding: 15px;
            text-align: center;
            font-size: 16px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
            margin-bottom: 12px;
        }

        /* Font resize rules */
        @media (max-width: 768px) {
            .card { font-size: 14px; padding: 12px; }
        }
        @media (max-width: 480px) {
            .card { font-size: 13px; padding: 10px; }
        }
        @media (max-width: 320px) {
            .card { font-size: 12px; padding: 8px; }
        }
    </style>
""", unsafe_allow_html=True)

# ---------- DEMO ----------
st.title("📱 Responsive Layout Demo (320px aware)")

# --- Cards Section ---
st.subheader("Cards Section")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">📊 Card 1</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="card">📈 Card 2</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="card">📂 Card 3</div>', unsafe_allow_html=True)

# --- Table Section ---
st.subheader("Responsive Table Example")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Diana"],
    "Age": [24, 30, 28, 35],
    "Dept": ["HR", "IT", "Finance", "Marketing"]
})
st.dataframe(df, use_container_width=True)

# --- Text Columns ---
st.subheader("Two Text Columns (stay side by side on phone)")
colA, colB = st.columns(2)
with colA:
    st.markdown('<div class="card">Left column text</div>', unsafe_allow_html=True)
with colB:
    st.markdown('<div class="card">Right column text</div>', unsafe_allow_html=True)
