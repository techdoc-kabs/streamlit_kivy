# # # app.py
# import streamlit as st
# import pandas as pd

# st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # Optional: try to detect width using streamlit-js-eval (not required)
# try:
#     from streamlit_js_eval import streamlit_js_eval
#     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# except Exception:
#     width = None

# # ---------- Global CSS: container, cards, responsive table ----------
# st.markdown(
#     """
#     <style>
#     /* ---------- Container + Cards ---------- */
#     .cards-wrap {
#       display: flex;
#       gap: 12px;
#       align-items: flex-start;
#       justify-content: flex-start;
#       flex-wrap: wrap;               /* allow wrapping */
#       padding: 8px 0;
#       box-sizing: border-box;
#     }

#     .card {
#       background: #ffffff;
#       border-radius: 10px;
#       box-shadow: 0 2px 10px rgba(0,0,0,0.06);
#       padding: 16px;
#       min-width: 160px;             /* prevents cards from going too narrow */
#       flex: 0 0 32%;                /* desktop: ~3 per row */
#       box-sizing: border-box;
#       transition: transform 0.12s ease;
#       overflow: hidden;
#     }
#     .card:hover { transform: translateY(-4px); }
#     .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
#     .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

#     /* ---------- Table ---------- */
#     .resp-table { width:100%; border-collapse: collapse; margin-top: 8px; }
#     .resp-table th, .resp-table td { padding: 8px 10px; border: 1px solid #e6e6e6; text-align:left; font-size:14px; }
#     .resp-table th { background:#0d1b3d; color:#fff; }

#     /* ---------- Breakpoints ---------- */
#     /* Tablet-ish: 3->2 */
#     @media (max-width: 992px) {
#       .card { flex: 0 0 48%; }      /* 2 cards per row */
#     }

#     /* Phones: ensure 2 columns side-by-side down to 321px */
#     @media (max-width: 768px) {
#       .card { flex: 0 0 48%; padding: 12px; min-width: 140px; }
#       .cards-wrap { gap: 8px; }
#       .resp-table th, .resp-table td { font-size:13px; padding: 6px 8px; }
#     }

#     /* Very small phones but still bigger than tiny: keep 2 col behavior */
#     @media (max-width: 480px) {
#       .card { flex: 0 0 48%; padding: 10px; min-width: 120px; }
#       .card h3 { font-size: 14px; }
#       .card p { font-size: 12px; }
#       .resp-table th, .resp-table td { font-size:12px; }
#     }

#     /* TINY phones (<= 320px) -> fallback to single column */
#     @media (max-width: 320px) {
#       .card { flex: 0 0 100%; min-width: 100%; }
#       .cards-wrap { gap: 6px; }
#       .card h3 { font-size: 13px; }
#       .card p { font-size: 11px; }
#     }

#     /* ---------- Responsive table -> stacked rows on tiny screens ---------- */
#     @media (max-width: 480px) {
#       .resp-table, .resp-table thead, .resp-table tbody, .resp-table th, .resp-table td, .resp-table tr {
#         display: block;
#         width: 100%;
#       }
#       .resp-table thead { display: none; } /* hide table header on small screens */
#       .resp-table tr { margin-bottom: 12px; border: 1px solid #eee; padding: 8px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.03); }
#       .resp-table td { display: flex; justify-content: space-between; padding: 8px 10px; }
#       .resp-table td:before { content: attr(data-label); font-weight:600; margin-right:8px; color:#555; }
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# # ---------- Dynamic rendering: use Streamlit native columns on large screens, custom container on smaller screens ----------
# LARGE_SCREEN_THRESHOLD = 992
# SMALL_SINGLE_COL_THRESHOLD = 320

# use_native_columns = False
# if width is not None:
#     st.write(f"📏 Detected browser width: {width}px")
#     if width >= LARGE_SCREEN_THRESHOLD:
#         use_native_columns = True
# else:
#     # width unknown: default to custom container (safe)
#     st.info("Screen width not detected — using responsive container (recommended).")

# # ------------- Option A: Streamlit native columns (desktop - optional) -------------
# if use_native_columns:
#     st.subheader("Native Streamlit columns (desktop)")
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         st.metric("Metric A", "120")
#         st.write("Description A")
#     with c2:
#         st.metric("Metric B", "72")
#         st.write("Description B")
#     with c3:
#         st.metric("Metric C", "45")
#         st.write("Description C")
#     st.markdown("---")

# # ------------- Option B: Custom HTML Container for cards (mobile-friendly) -------------
# st.subheader("Cards (custom container — controlled by our CSS)")
# cards = [
#     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
#     {"title": "Analytics", "body": "Interactive charts and trends overview."},
#     {"title": "Archives", "body": "Browse archived documents and files."},
#     {"title": "Team", "body": "Quick team stats and availability."}
# ]

# # Build HTML for cards
# cards_html = '<div class="cards-wrap">'
# for c in cards:
#     cards_html += f'''<div class="card">
#         <h3>{c["title"]}</h3>
#         <p>{c["body"]}</p>
#       </div>
#     '''
# cards_html += "</div>"

# st.markdown(cards_html, unsafe_allow_html=True)

# # ---------- Responsive Table (HTML) ----------
# import streamlit as st
# import pandas as pd

# st.set_page_config(layout="wide")
# st.title("Responsive Table with 10 Columns (auto-fit)")

# # Sample DataFrame with 10 columns
# df = pd.DataFrame({
#     "ID": [1,2,3,4],
#     "Name": ["Alice", "Bob", "Charlie", "Diana"],
#     "Age": [24, 30, 28, 35],
#     "Department": ["HR", "IT", "Finance", "Marketing"],
#     "Position": ["Manager", "Developer", "Analyst", "Designer"],
#     "Location": ["NY", "LA", "Chicago", "Houston"],
#     "Experience": [5, 7, 3, 6],
#     "Salary": ["50k", "70k", "45k", "60k"],
#     "Projects": [3, 5, 2, 4],
#     "Status": ["Active", "Active", "Inactive", "Active"]
# })

# # CSS for responsive table
# st.markdown("""
#     <style>
#     .resp-table-fixed {
#         width: 100% !important;
#         border-collapse: collapse;
#         table-layout: fixed; /* ensures columns shrink to fit */
#     }
#     .resp-table-fixed th, .resp-table-fixed td {
#         padding: 8px 10px;
#         border: 1px solid #ddd;
#         overflow-wrap: break-word; /* wrap long content */
#         text-align: left;
#         font-size: 14px;
#     }
#     .resp-table-fixed th {
#         background-color: #0d1b3d;
#         color: white;
#     }

#     /* Smaller font on mobile */
#     @media (max-width: 768px) {
#         .resp-table-fixed th, .resp-table-fixed td {
#             font-size: 12px;
#             padding: 6px 8px;
#         }
#     }

#     /* Very small phones */
#     @media (max-width: 480px) {
#         .resp-table-fixed th, .resp-table-fixed td {
#             font-size: 11px;
#             padding: 4px 6px;
#         }
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Render table as HTML
# table_html = '<table class="resp-table-fixed">'
# table_html += '<thead><tr>' + ''.join(f'<th>{col}</th>' for col in df.columns) + '</tr></thead>'
# table_html += '<tbody>'
# for _, row in df.iterrows():
#     table_html += '<tr>' + ''.join(f'<td>{row[col]}</td>' for col in df.columns) + '</tr>'
# table_html += '</tbody></table>'

# st.markdown(table_html, unsafe_allow_html=True)
# import streamlit as st
# import pandas as pd
# from streamlit_card import card
# from streamlit_js_eval import streamlit_js_eval

# st.set_page_config(layout="wide")
# st.title("Responsive Streamlit Cards + Table Demo")

# # ---------- Detect screen width ----------
# try:
#     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_WIDTH")
# except Exception:
#     width = 768  # fallback width

# st.write(f"📏 Detected screen width: {width}px")

# # ---------- Decide card width dynamically ----------
# if width >= 992:
#     card_width = 300
# elif width >= 481:
#     card_width = 48  # percent
# else:
#     card_width = 90  # percent for tiny phones

# # ---------- Cards Data ----------
# cards_data = [
#     {"title": "Reports", "text": "View latest reports.", "image": "https://placekitten.com/300/300"},
#     {"title": "Analytics", "text": "Explore charts.", "image": "https://placekitten.com/301/300"},
#     {"title": "Archives", "text": "Browse files.", "image": "https://placekitten.com/302/300"},
#     {"title": "Team", "text": "Team stats.", "image": "https://placekitten.com/303/300"},
#     {"title": "Projects", "text": "Project overview.", "image": "https://placekitten.com/304/300"},
#     {"title": "Settings", "text": "App configuration.", "image": "https://placekitten.com/305/300"},
# ]

# st.subheader("Clickable Streamlit Cards")

# # ---------- Render streamlit-card components ----------
# clicked_card = None
# for idx, c in enumerate(cards_data):
#     res = card(
#         title=c["title"],
#         text=c["text"],
#         image=c["image"],
#         styles={
#             "card": {
#                 "width": f"{card_width}px" if width >= 992 else f"{card_width}%",
#                 "height": "300px",
#                 "border-radius": "20px",
#                 "box-shadow": "0 0 10px rgba(0,0,0,0.3)",
#                 "margin": "10px auto",
#                 "display": "flex",
#                 "flex-direction": "column",
#                 "align-items": "center",
#                 "justify-content": "center",
#                 "overflow": "hidden"
#             },
#             "filter": {"background-color": "rgba(0, 0, 0, 0)"},
#             "title": {"font-size": "18px"},
#             "text": {"font-size": "14px"}
#         }
#     )
#     if res:
#         clicked_card = c["title"]

# if clicked_card:
#     st.success(f"You clicked on: {clicked_card}!")

# # ---------- Responsive Table Section ----------
# st.subheader("Responsive 10-Column Table")
# df = pd.DataFrame({
#     "ID": [1,2,3,4],
#     "Name": ["Alice", "Bob", "Charlie", "Diana"],
#     "Age": [24, 30, 28, 35],
#     "Department": ["HR", "IT", "Finance", "Marketing"],
#     "Position": ["Manager", "Developer", "Analyst", "Designer"],
#     "Location": ["NY", "LA", "Chicago", "Houston"],
#     "Experience": [5, 7, 3, 6],
#     "Salary": ["50k", "70k", "45k", "60k"],
#     "Projects": [3, 5, 2, 4],
#     "Status": ["Active", "Active", "Inactive", "Active"]
# })

# # CSS for responsive table
# st.markdown("""
#     <style>
#     .resp-table-fixed {
#         width: 100% !important;
#         border-collapse: collapse;
#         table-layout: fixed;
#     }
#     .resp-table-fixed th, .resp-table-fixed td {
#         padding: 8px 10px;
#         border: 1px solid #ddd;
#         overflow-wrap: break-word;
#         text-align: left;
#         font-size: 14px;
#     }
#     .resp-table-fixed th { background-color:#0d1b3d; color:white; }
#     @media (max-width: 768px) {
#         .resp-table-fixed th, .resp-table-fixed td { font-size:12px; padding:6px 8px; }
#     }
#     @media (max-width: 480px) {
#         .resp-table-fixed th, .resp-table-fixed td { font-size:11px; padding:4px 6px; }
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Render HTML table
# table_html = '<table class="resp-table-fixed">'
# table_html += '<thead><tr>' + ''.join(f'<th>{col}</th>' for col in df.columns) + '</tr></thead>'
# table_html += '<tbody>'
# for _, row in df.iterrows():
#     table_html += '<tr>' + ''.join(f'<td>{row[col]}</td>' for col in df.columns) + '</tr>'
# table_html += '</tbody></table>'
# st.markdown(table_html, unsafe_allow_html=True)

# import streamlit as st
# import pandas as pd

# st.set_page_config(layout="wide", page_title="Responsive Cards + Table Demo")

# st.title("📊 Responsive Cards + Table Demo")

# # ---------- Detect screen width (optional) ----------
# try:
#     from streamlit_js_eval import streamlit_js_eval
#     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_WIDTH")
# except Exception:
#     width = None

# if width:
#     st.write(f"📏 Detected browser width: {width}px")

# # ---------- Global CSS for cards and table ----------
# st.markdown("""
# <style>
# /* ---------- Cards Container ---------- */
# .cards-wrap {
#     display: flex;
#     flex-wrap: wrap;
#     gap: 16px;
#     justify-content: flex-start;
# }

# .card-html {
#     background: #fff;
#     border-radius: 12px;
#     box-shadow: 0 2px 10px rgba(0,0,0,0.1);
#     flex: 0 0 32%; /* desktop: 3 per row */
#     min-width: 180px;
#     padding: 12px;
#     text-align: center;
#     transition: transform 0.2s ease;
#     cursor: pointer;
# }
# .card-html:hover {
#     transform: translateY(-6px);
# }

# /* Card title and text */
# .card-html h3 {
#     margin: 8px 0;
#     font-size: clamp(16px, 1.5vw, 20px);
# }
# .card-html p {
#     margin: 4px 0;
#     font-size: clamp(13px, 1.1vw, 15px);
#     color: #333;
# }

# /* ---------- Responsive Breakpoints ---------- */
# @media (max-width: 992px) {
#     .card-html { flex: 0 0 48%; }
# }
# @media (max-width: 480px) {
#     .card-html { flex: 0 0 48%; min-width: 140px; }
# }
# @media (max-width: 320px) {
#     .card-html { flex: 0 0 100%; }
# }

# /* ---------- Responsive Table ---------- */
# .resp-table-fixed {
#     width: 100% !important;
#     border-collapse: collapse;
#     table-layout: fixed;
# }
# .resp-table-fixed th, .resp-table-fixed td {
#     padding: 8px 10px;
#     border: 1px solid #ddd;
#     overflow-wrap: break-word;
#     text-align: left;
#     font-size: 14px;
# }
# .resp-table-fixed th { background-color:#0d1b3d; color:white; }
# @media (max-width: 768px) {
#     .resp-table-fixed th, .resp-table-fixed td { font-size:12px; padding:6px 8px; }
# }
# @media (max-width: 480px) {
#     .resp-table-fixed th, .resp-table-fixed td { font-size:11px; padding:4px 6px; }
# }
# </style>
# """, unsafe_allow_html=True)

# # ---------- Cards Data ----------
# cards_data = [
#     {"title": "Reports", "text": "View latest reports.", "image": "https://placekitten.com/300/200"},
#     {"title": "Analytics", "text": "Explore charts.", "image": "https://placekitten.com/301/200"},
#     {"title": "Archives", "text": "Browse files.", "image": "https://placekitten.com/302/200"},
#     {"title": "Team", "text": "Team stats.", "image": "https://placekitten.com/303/200"},
#     {"title": "Projects", "text": "Project overview.", "image": "https://placekitten.com/304/200"},
#     {"title": "Settings", "text": "App configuration.", "image": "https://placekitten.com/305/200"},
# ]

# # ---------- Render Cards ----------
# st.subheader("📂 Responsive Cards Section")

# cards_html = '<div class="cards-wrap">'
# for idx, c in enumerate(cards_data):
#     cards_html += f'''
#     <div class="card-html" onclick="window.alert('You clicked: {c["title"]}')">
#         <h3>{c["title"]}</h3>
#         <p>{c["text"]}</p>
#         <img src="{c["image"]}" width="100%" style="border-radius:8px; margin-top:6px;" />
#     </div>
#     '''
# cards_html += '</div>'

# st.markdown(cards_html, unsafe_allow_html=True)

# # ---------- Sample 10-Column Table ----------
# st.subheader("📋 Responsive 10-Column Table")
# df = pd.DataFrame({
#     "ID": [1,2,3,4],
#     "Name": ["Alice", "Bob", "Charlie", "Diana"],
#     "Age": [24, 30, 28, 35],
#     "Department": ["HR", "IT", "Finance", "Marketing"],
#     "Position": ["Manager", "Developer", "Analyst", "Designer"],
#     "Location": ["NY", "LA", "Chicago", "Houston"],
#     "Experience": [5, 7, 3, 6],
#     "Salary": ["50k", "70k", "45k", "60k"],
#     "Projects": [3, 5, 2, 4],
#     "Status": ["Active", "Active", "Inactive", "Active"]
# })

# table_html = '<table class="resp-table-fixed">'
# table_html += '<thead><tr>' + ''.join(f'<th>{col}</th>' for col in df.columns) + '</tr></thead>'
# table_html += '<tbody>'
# for _, row in df.iterrows():
#     table_html += '<tr>' + ''.join(f'<td>{row[col]}</td>' for col in df.columns) + '</tr>'
# table_html += '</tbody></table>'

# st.markdown(table_html, unsafe_allow_html=True)
import streamlit as st
from streamlit_card import card
from streamlit_javascript import st_javascript

# ---------------- DEVICE DETECTION ----------------
device_width = st_javascript("window.innerWidth", key="screen_width") or 1024
is_mobile = device_width < 704  # mobile if width < 704px

# ---------------- RESPONSIVE CSS ----------------
st.markdown("""
<style>
.cards-wrap {
    display: flex;
    flex-wrap: wrap;       /* allow cards to wrap */
    gap: 12px;
    padding: 0;
    margin: 0;
    justify-content: flex-start;
    box-sizing: border-box;
}
.cards-wrap > div {
    flex: 0 0 48%;         /* two cards per row */
    min-width: 140px;
    box-sizing: border-box;
}
@media (max-width: 320px) {
    .cards-wrap > div {
        flex: 0 0 48%;      /* still force two columns for tiny phones */
        min-width: 48%;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- DISPLAY FUNCTION ----------------
def display_card_menu(options: list, session_key: str, next_screen=None):
    if not is_mobile:
        # Desktop: native columns
        cols = st.columns(4, gap="small")
        for idx, option in enumerate(options):
            with cols[idx % 4]:
                clicked = card(
                    title=option.get("title", ""),
                    text=option.get("text", ""),
                    key=f"{session_key}-{option.get('text','')}",
                    styles={
                        "card": {
                            "width": "100%", "height": "200px",
                            "border-radius": "6px",
                            "background": "#3498db",
                            "color": "white",
                            "box-shadow": "0 4px 12px rgba(0,0,0,0.25)",
                            "text-align": "center",
                        },
                        "text": {"font-size": "18px"},
                        "title": {"font-size": "30px"},
                    }
                )
                if clicked:
                    st.session_state[session_key] = option.get("text")
                    if next_screen:
                        st.session_state.screen = next_screen
                    st.session_state["__nav_triggered"] = True
                    return True
    else:
        # Mobile: flex-wrap container
        st.markdown('<div class="cards-wrap">', unsafe_allow_html=True)
        for idx, option in enumerate(options):
            st.markdown(f'<div>', unsafe_allow_html=True)
            clicked = card(
                title=option.get("title", ""),
                text=option.get("text", ""),
                key=f"{session_key}-{option.get('text','')}",
                styles={
                    "card": {
                        "width": "100%", "height": "150px",
                        "border-radius": "6px",
                        "background": "#3498db",
                        "color": "white",
                        "box-shadow": "0 4px 12px rgba(0,0,0,0.25)",
                        "text-align": "center",
                    },
                    "text": {"font-size": "16px"},
                    "title": {"font-size": "24px"},
                }
            )
            if clicked:
                st.session_state[session_key] = option.get("text")
                if next_screen:
                    st.session_state.screen = next_screen
                st.session_state["__nav_triggered"] = True
                return True
            st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    return False

# ---------------- APP ----------------
st.title("Responsive Card Menu Example")

if "screen" not in st.session_state:
    st.session_state["screen"] = "main_menu"

options = [
    {"title": "🗓️", "text": "Schedules"},
    {"title": "📚", "text": "Reports"},
    {"title": "📈", "text": "Analysis"},
    {"title": "📧", "text": "Messages"},
    {"title": "🗃️", "text": "Files"},
    {"title": "🗄️", "text": "Resources"},
]

clicked = display_card_menu(options, session_key="selected_page")

if clicked:
    st.success(f"You clicked: {st.session_state['selected_page']}")



