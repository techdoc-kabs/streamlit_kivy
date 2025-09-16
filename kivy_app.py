import streamlit as st

st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# ---------- CSS (same as your design) ----------
st.markdown("""
<style>
.cards-wrap {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  padding: 8px 0;
}
.card {
  background: #fff;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.06);
  padding: 16px;
  min-width: 160px;
  flex: 0 0 40%;
  transition: transform 0.12s ease;
  overflow: hidden;
}
.card:hover { transform: translateY(-4px); }
.card h3 { margin:6px 0; font-size: clamp(16px,1.6vw,20px);}
.card p { margin:4px 0; font-size: clamp(13px,1.1vw,15px); color:#333; }
@media (max-width:992px){.card{flex:0 0 48%;}}
@media (max-width:480px){.card{flex:0 0 48%; padding:10px; min-width:120px;}}
@media (max-width:350px){.card{flex:0 0 120%; padding:10px; min-width:120px;}}
@media (max-width: 480px){
  .cards-wrap {
    justify-content: center;  /* center cards horizontally */
  }
}
</style>
""", unsafe_allow_html=True)

# ---------- Cards data ----------
cards = [
    {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
    {"title": "Analytics", "body": "Interactive charts and trends overview."},
    {"title": "Archives", "body": "Browse archived documents and files."},
    {"title": "Team", "body": "Quick team stats and availability."}
]

# ---------- Session State ----------
if "clicked_card" not in st.session_state:
    st.session_state.clicked_card = None

# Detect URL param
query_params = st.experimental_get_query_params()
if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
    st.session_state.clicked_card = query_params.get("nav")[0]

# ---------- Cache cards HTML ----------
@st.cache_data
def build_cards_html(clicked_card=None):
    html = '<div class="cards-wrap">'
    for c in cards:
        highlight = "border: 2px solid #4CAF50;" if clicked_card == c["title"].lower() else ""
        html += f'''<a href="/?nav={c["title"].lower()}" style="text-decoration:none; color:inherit; flex:0 0 32%;">
            <div class="card" style="{highlight}">
                <h3>{c["title"]}</h3>
                <p>{c["body"]}</p>
            </div>
        </a>
        '''
    html += "</div>"
    return html

# ---------- Page Rendering ----------
if st.session_state.clicked_card is None:
    st.title("Responsive Cards Menu")
    st.markdown(build_cards_html(), unsafe_allow_html=True)
else:
    st.title(f"{st.session_state.clicked_card.title()} Page")
    st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

    # Only show the back button here
    if st.button("⬅ Back to Menu"):
        st.session_state.clicked_card = None
        st.experimental_set_query_params()
        st.rerun()





