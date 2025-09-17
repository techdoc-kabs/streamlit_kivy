# # # # import streamlit as st
# # # # import pandas as pd

# # # # st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # # # # Optional: try to detect width using streamlit-js-eval (not required)
# # # # try:
# # # #     from streamlit_js_eval import streamlit_js_eval
# # # #     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# # # # except Exception:
# # # #     width = None

# # # # # ---------- Global CSS: container, cards, responsive table ----------
# # # # st.markdown(
# # # #     """
# # # #     <style>
# # # #     /* ---------- Container + Cards ---------- */
# # # #     .cards-wrap {
# # # #       display: flex;
# # # #       gap: 12px;
# # # #       align-items: flex-start;
# # # #       justify-content: flex-start;
# # # #       flex-wrap: wrap;               /* allow wrapping */
# # # #       padding: 8px 0;
# # # #       box-sizing: border-box;
# # # #     }

# # # #     .card {
# # # #       background: #ffffff;
# # # #       border-radius: 10px;
# # # #       box-shadow: 0 2px 10px rgba(0,0,0,0.06);
# # # #       padding: 16px;
# # # #       min-width: 160px;             /* prevents cards from going too narrow */
# # # #       flex: 0 0 32%;                /* desktop: ~3 per row */
# # # #       box-sizing: border-box;
# # # #       transition: transform 0.12s ease;
# # # #       overflow: hidden;
# # # #     }
# # # #     .card:hover { transform: translateY(-4px); }
# # # #     .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
# # # #     .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

# # # #     /* ---------- Table ---------- */
# # # #     .resp-table { width:100%; border-collapse: collapse; margin-top: 8px; }
# # # #     .resp-table th, .resp-table td { padding: 8px 10px; border: 1px solid #e6e6e6; text-align:left; font-size:14px; }
# # # #     .resp-table th { background:#0d1b3d; color:#fff; }

# # # #     /* ---------- Breakpoints ---------- */
# # # #     /* Tablet-ish: 3->2 */
# # # #     @media (max-width: 992px) {
# # # #       .card { flex: 0 0 48%; }      /* 2 cards per row */
# # # #     }

# # # #     /* Phones: ensure 2 columns side-by-side down to 321px */
# # # #     @media (max-width: 768px) {
# # # #       .card { flex: 0 0 48%; padding: 12px; min-width: 140px; }
# # # #       .cards-wrap { gap: 8px; }
# # # #       .resp-table th, .resp-table td { font-size:13px; padding: 6px 8px; }
# # # #     }

# # # #     /* Very small phones but still bigger than tiny: keep 2 col behavior */
# # # #     @media (max-width: 480px) {
# # # #       .card { flex: 0 0 48%; padding: 10px; min-width: 120px; }
# # # #       .card h3 { font-size: 14px; }
# # # #       .card p { font-size: 12px; }
# # # #       .resp-table th, .resp-table td { font-size:12px; }
# # # #     }

# # # #     /* TINY phones (<= 320px) -> fallback to single column */
# # # #     @media (max-width: 320px) {
# # # #       .card { flex: 0 0 100%; min-width: 100%; }
# # # #       .cards-wrap { gap: 6px; }
# # # #       .card h3 { font-size: 13px; }
# # # #       .card p { font-size: 11px; }
# # # #     }

# # # #     /* ---------- Responsive table -> stacked rows on tiny screens ---------- */
# # # #     @media (max-width: 480px) {
# # # #       .resp-table, .resp-table thead, .resp-table tbody, .resp-table th, .resp-table td, .resp-table tr {
# # # #         display: block;
# # # #         width: 100%;
# # # #       }
# # # #       .resp-table thead { display: none; } /* hide table header on small screens */
# # # #       .resp-table tr { margin-bottom: 12px; border: 1px solid #eee; padding: 8px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.03); }
# # # #       .resp-table td { display: flex; justify-content: space-between; padding: 8px 10px; }
# # # #       .resp-table td:before { content: attr(data-label); font-weight:600; margin-right:8px; color:#555; }
# # # #     }
# # # #     </style>
# # # #     """,
# # # #     unsafe_allow_html=True,
# # # # )

# # # # st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# # # # # ---------- Dynamic rendering: use Streamlit native columns on large screens, custom container on smaller screens ----------
# # # # LARGE_SCREEN_THRESHOLD = 992
# # # # SMALL_SINGLE_COL_THRESHOLD = 320

# # # # use_native_columns = False
# # # # if width is not None:
# # # #     st.write(f"📏 Detected browser width: {width}px")
# # # #     if width >= LARGE_SCREEN_THRESHOLD:
# # # #         use_native_columns = True
# # # # else:
# # # #     # width unknown: default to custom container (safe)
# # # #     st.info("Screen width not detected — using responsive container (recommended).")

# # # # # ------------- Option A: Streamlit native columns (desktop - optional) -------------
# # # # if use_native_columns:
# # # #     st.subheader("Native Streamlit columns (desktop)")
# # # #     c1, c2, c3 = st.columns(3)
# # # #     with c1:
# # # #         st.metric("Metric A", "120")
# # # #         st.write("Description A")
# # # #     with c2:
# # # #         st.metric("Metric B", "72")
# # # #         st.write("Description B")
# # # #     with c3:
# # # #         st.metric("Metric C", "45")
# # # #         st.write("Description C")
# # # #     st.markdown("---")



# # # # # # Cards data
# # # # cards = [
# # # #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# # # #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# # # #     {"title": "Archives", "body": "Browse archived documents and files."},
# # # #     {"title": "Team", "body": "Quick team stats and availability."}
# # # # ]

# # # # # ---------- Detect clicked card ----------
# # # # query_params = st.experimental_get_query_params()
# # # # clicked_card = query_params.get("nav", [None])[0]

# # # # # ---------- Page Routing ----------
# # # # if not clicked_card:
# # # #     # Show card menu
# # # #     st.title("Responsive Cards Menu")
# # # #     cards_html = '<div class="cards-wrap">'
# # # #     for c in cards:
# # # #         cards_html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# # # #             <div class="card">
# # # #                 <h3>{c["title"]}</h3>
# # # #                 <p>{c["body"]}</p>
# # # #             </div>
# # # #         </a>
# # # #         '''
# # # #     cards_html += "</div>"
# # # #     st.markdown(cards_html, unsafe_allow_html=True)

# # # # else:
# # # #     # Show detail page for the clicked card
# # # #     st.title(f"{clicked_card.title()} Page")
# # # #     st.write(f"This is the detailed view for **{clicked_card.title()}**.")
# # # #     # Back link
# # # #     st.markdown(
# # # #         '<a href="/" target="_self" style="text-decoration:none; color:#4CAF50;">⬅ Back to Menu</a>',
# # # #         unsafe_allow_html=True,
# # # #     )
# # # import streamlit as st
# # # import pandas as pd

# # # st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # # # Optional: detect width
# # # try:
# # #     from streamlit_js_eval import streamlit_js_eval
# # #     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# # # except Exception:
# # #     width = None

# # # # ---------- Global CSS (unchanged) ----------
# # # st.markdown("""
# # # <style>
# # # .cards-wrap {
# # #   display: flex;
# # #   gap: 12px;
# # #   align-items: flex-start;
# # #   justify-content: flex-start;
# # #   flex-wrap: wrap;
# # #   padding: 8px 0;
# # #   box-sizing: border-box;
# # # }
# # # .card {
# # #   background: #ffffff;
# # #   border-radius: 10px;
# # #   box-shadow: 0 2px 10px rgba(0,0,0,0.06);
# # #   padding: 16px;
# # #   min-width: 160px;
# # #   flex: 0 0 32%;
# # #   box-sizing: border-box;
# # #   transition: transform 0.12s ease;
# # #   overflow: hidden;
# # # }
# # # .card:hover { transform: translateY(-4px); }
# # # .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
# # # .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }
# # # .resp-table { width:100%; border-collapse: collapse; margin-top: 8px; }
# # # .resp-table th, .resp-table td { padding: 8px 10px; border: 1px solid #e6e6e6; text-align:left; font-size:14px; }
# # # .resp-table th { background:#0d1b3d; color:#fff; }
# # # @media (max-width: 992px) { .card { flex: 0 0 48%; } }
# # # @media (max-width: 768px) { .card { flex: 0 0 48%; padding:12px; min-width:140px; } .cards-wrap { gap:8px; } .resp-table th, .resp-table td { font-size:13px; padding:6px 8px; } }
# # # @media (max-width: 480px) { .card { flex: 0 0 48%; padding:10px; min-width:120px; } .card h3 { font-size:14px; } .card p { font-size:12px; } .resp-table th, .resp-table td { font-size:12px; } }
# # # @media (max-width: 320px) { .card { flex:0 0 100%; min-width:100%; } .cards-wrap { gap:6px; } .card h3 { font-size:13px; } .card p { font-size:11px; } }
# # # @media (max-width: 480px) {
# # #     .resp-table, .resp-table thead, .resp-table tbody, .resp-table th, .resp-table td, .resp-table tr { display: block; width: 100%; }
# # #     .resp-table thead { display: none; }
# # #     .resp-table tr { margin-bottom: 12px; border: 1px solid #eee; padding:8px; border-radius:8px; box-shadow:0 1px 4px rgba(0,0,0,0.03);}
# # #     .resp-table td { display: flex; justify-content: space-between; padding:8px 10px;}
# # #     .resp-table td:before { content: attr(data-label); font-weight:600; margin-right:8px; color:#555; }
# # # }
# # # </style>
# # # """, unsafe_allow_html=True)

# # # # ---------- Screen width handling ----------
# # # LARGE_SCREEN_THRESHOLD = 992
# # # use_native_columns = False
# # # if width is not None:
# # #     st.write(f"📏 Detected browser width: {width}px")
# # #     if width >= LARGE_SCREEN_THRESHOLD:
# # #         use_native_columns = True
# # # else:
# # #     st.info("Screen width not detected — using responsive container.")

# # # # ------------- Option A: Streamlit native columns (desktop) -------------
# # # if use_native_columns:
# # #     st.subheader("Native Streamlit columns (desktop)")
# # #     c1, c2, c3 = st.columns(3)
# # #     with c1:
# # #         st.metric("Metric A", "120")
# # #         st.write("Description A")
# # #     with c2:
# # #         st.metric("Metric B", "72")
# # #         st.write("Description B")
# # #     with c3:
# # #         st.metric("Metric C", "45")
# # #         st.write("Description C")
# # #     st.markdown("---")

# # # # ---------- Cards data ----------
# # # cards = [
# # #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# # #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# # #     {"title": "Archives", "body": "Browse archived documents and files."},
# # #     {"title": "Team", "body": "Quick team stats and availability."}
# # # ]

# # # # ---------- Session-state clicked card ----------
# # # if "clicked_card" not in st.session_state:
# # #     st.session_state.clicked_card = None

# # # # ---------- Detect click via query param (only if no card selected yet) ----------
# # # query_params = st.experimental_get_query_params()
# # # if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
# # #     st.session_state.clicked_card = query_params.get("nav")[0]

# # # # ---------- Page rendering ----------
# # # if st.session_state.clicked_card is None:
# # #     # Show cards menu
# # #     st.title("Responsive Cards Menu")

# # #     cards_html = '<div class="cards-wrap">'
# # #     for c in cards:
# # #         cards_html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# # #             <div class="card">
# # #                 <h3>{c["title"]}</h3>
# # #                 <p>{c["body"]}</p>
# # #             </div>
# # #         </a>
# # #         '''
# # #     cards_html += "</div>"
# # #     st.markdown(cards_html, unsafe_allow_html=True)

# # # else:
# # #     # Show detail page
# # #     st.title(f"{st.session_state.clicked_card.title()} Page")
# # #     st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

# # #     # Back button
# # #     if st.button("⬅ Back to Menu"):
# # #         st.session_state.clicked_card = None
# # #         st.experimental_set_query_params()  # <- clears URL parameter so you can return
# # #         st.rerun()


# # import streamlit as st
# # import pandas as pd

# # st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # # Optional: detect width
# # try:
# #     from streamlit_js_eval import streamlit_js_eval
# #     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# # except Exception:
# #     width = None

# # # ---------- Global CSS: container, cards, responsive table ----------
# # st.markdown(
# #     """
# #     <style>
# #     .cards-wrap {
# #       display: flex;
# #       gap: 12px;
# #       align-items: flex-start;
# #       justify-content: flex-start;
# #       flex-wrap: wrap;
# #       padding: 8px 0;
# #       box-sizing: border-box;
# #     }
# #     .card {
# #       background: #ffffff;
# #       border-radius: 10px;
# #       box-shadow: 0 2px 10px rgba(0,0,0,0.06);
# #       padding: 16px;
# #       min-width: 160px;
# #       flex: 0 0 32%;
# #       box-sizing: border-box;
# #       transition: transform 0.12s ease;
# #       overflow: hidden;
# #     }
# #     .card:hover { transform: translateY(-4px); }
# #     .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
# #     .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

# #     /* Table styling omitted for brevity (keep your original CSS) */

# #     @media (max-width: 992px) { .card { flex: 0 0 48%; } }
# #     @media (max-width: 768px) { .card { flex: 0 0 48%; padding: 12px; min-width: 140px; } }
# #     @media (max-width: 480px) { .card { flex: 0 0 48%; padding: 10px; min-width: 120px; } }
# #     @media (max-width: 320px) { .card { flex: 0 0 100%; min-width: 100%; } }
# #     </style>
# #     """,
# #     unsafe_allow_html=True,
# # )

# # st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# # # ---------- Dynamic rendering: large vs small screen ----------
# # LARGE_SCREEN_THRESHOLD = 992
# # use_native_columns = False
# # if width is not None:
# #     st.write(f"📏 Detected browser width: {width}px")
# #     if width >= LARGE_SCREEN_THRESHOLD:
# #         use_native_columns = True
# # else:
# #     st.info("Screen width not detected — using responsive container.")

# # # ------------- Option A: Streamlit native columns (desktop) -------------
# # if use_native_columns:
# #     st.subheader("Native Streamlit columns (desktop)")
# #     c1, c2, c3 = st.columns(3)
# #     with c1:
# #         st.metric("Metric A", "120")
# #         st.write("Description A")
# #     with c2:
# #         st.metric("Metric B", "72")
# #         st.write("Description B")
# #     with c3:
# #         st.metric("Metric C", "45")
# #         st.write("Description C")
# #     st.markdown("---")

# # # ---------- Cards data ----------
# # # cards = [
# # #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# # #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# # #     {"title": "Archives", "body": "Browse archived documents and files."},
# # #     {"title": "Team", "body": "Quick team stats and availability."}
# # # ]

# # # # ---------- Session-state clicked card ----------
# # # if "clicked_card" not in st.session_state:
# # #     st.session_state.clicked_card = None

# # # # Only update clicked_card if session_state is empty
# # # query_params = st.experimental_get_query_params()
# # # if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
# # #     st.session_state.clicked_card = query_params.get("nav")[0]

# # # # ---------- Memoized function to build cards HTML ----------
# # # # ---------- Memoized function to build cards HTML ----------
# # # @st.cache_data
# # # def get_cards_html(clicked=None):
# # #     html = '<div class="cards-wrap">'
# # #     for c in cards:
# # #         highlight_style = "border: 2px solid #4CAF50;" if clicked == c["title"].lower() else ""
# # #         html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# # #             <div class="card" style="{highlight_style}">
# # #                 <h3>{c["title"]}</h3>
# # #                 <p>{c["body"]}</p>
# # #             </div>
# # #         </a>
# # #         '''
# # #     html += "</div>"
# # #     return html

# # # # ---------- Page rendering ----------
# # # if st.session_state.clicked_card is None:
# # #     # Show cards menu
# # #     st.title("Responsive Cards Menu")
# # #     st.markdown(get_cards_html(), unsafe_allow_html=True)
# # # else:
# # #     # Show detailed card page
# # #     st.title(f"{st.session_state.clicked_card.title()} Page")
# # #     st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

# # #     # Back button
# # #     if st.button("⬅ Back to Menu"):
# # #         st.session_state.clicked_card = None
# # #         st.experimental_set_query_params()  # clear URL
# # #         st.rerun()
# # # #


# # import streamlit as st

# # # ---------- Cards & submenus ----------
# # cards = [
# #     {"title": "Reports", "body": "Summary of recent reports.", "submenu": ["Financial", "Activity"]},
# #     {"title": "Analytics", "body": "Interactive charts.", "submenu": []},
# #     {"title": "Archives", "body": "Browse archived documents.", "submenu": []},
# #     {"title": "Team", "body": "Quick team stats.", "submenu": []}
# # ]

# # # ---------- Session state ----------
# # if "nav_stack" not in st.session_state:
# #     st.session_state.nav_stack = []  # navigation history

# # # ---------- Handle card clicks ----------
# # query_params = st.experimental_get_query_params()
# # clicked = query_params.get("nav", [None])[0]

# # if clicked:
# #     st.session_state.nav_stack.append(clicked)
# #     st.experimental_set_query_params()  # clear query param
# #     st.rerun()

# # # ---------- Current level ----------
# # current_level = st.session_state.nav_stack[-1] if st.session_state.nav_stack else None

# # # ---------- Global CSS ----------
# # st.markdown("""
# # <style>
# # .cards-wrap { display: flex; gap: 12px; flex-wrap: wrap; padding:8px 0; justify-content:flex-start; }
# # .card { background:#fff; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.06); padding:16px; min-width:160px; flex:0 0 32%; transition: transform 0.12s ease; overflow:hidden; }
# # .card:hover { transform: translateY(-4px); }
# # .card h3 { margin:6px 0; font-size:clamp(16px,1.6vw,20px); }
# # .card p { margin:4px 0; font-size:clamp(13px,1.1vw,15px); color:#333; }
# # @media (max-width:992px){ .card{ flex:0 0 48%; } }
# # @media (max-width:480px){ .cards-wrap{ justify-content: space-around; } .card{ flex:0 0 48%; padding:14px; min-width:140px;} .card h3{ font-size:16px;} .card p{ font-size:14px; } }
# # @media (max-width:350px){ .cards-wrap{ justify-content: space-around; } .card{ flex:0 0 48%; padding:12px; min-width:120px;} .card h3{ font-size:15px;} .card p{ font-size:13px; } }
# # </style>
# # """, unsafe_allow_html=True)

# # # ---------- Memoized HTML ----------
# # @st.cache_data
# # def get_cards_html(cards_list):
# #     html = '<div class="cards-wrap">'
# #     for c in cards_list:
# #         html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# #             <div class="card">
# #                 <h3>{c["title"]}</h3>
# #                 <p>{c.get("body","")}</p>
# #             </div>
# #         </a>'''
# #     html += "</div>"
# #     return html

# # # ---------- Helper to find card ----------
# # def find_card(title):
# #     for c in cards:
# #         if c["title"].lower() == title:
# #             return c
# #         if "submenu" in c and title in [s.lower() for s in c["submenu"]]:
# #             return {"title": title, "body": f"{title.title()} report.", "submenu": []}
# #     return None

# # # ---------- Page rendering ----------
# # # if not current_level:
# # #     # Main menu
# # #     st.title("Main Menu")
# # #     st.markdown(get_cards_html(cards), unsafe_allow_html=True)
# # # else:
# # #     card_obj = find_card(current_level)

# # #     if card_obj.get("submenu"):
# # #         # Show submenu
# # #         st.title(f"{card_obj['title']} Submenu")
# # #         sub_cards = [{"title": s, "body": f"{s} report."} for s in card_obj["submenu"]]
# # #         st.markdown(get_cards_html(sub_cards), unsafe_allow_html=True)
# # #     else:
# # #         # Final page
# # #         st.title(f"{card_obj['title']} Page")
# # #         st.write(f"This is the detailed view for **{card_obj['title']}**.")

# # #     # Back button always works
# # #     if st.button("⬅ Back"):
# # #         st.session_state.nav_stack.pop()  # go back
# # #         st.rerun()
# # if not current_level:
# #     # Main menu
# #     # st.title("Main Menu")
# #     # st.markdown(get_cards_html(cards), unsafe_allow_html=True)
# #     # if not current_level:
# #     # Main menu
# #     # st.title("Main Menu")

# #     # ---------- Introductory image ----------
# #     st.image("images/std.jpg", use_column_width=True, height=400)  # responsive width

# #     # Display cards
# #     st.markdown(get_cards_html(cards), unsafe_allow_html=True)


# # else:
# #     card_obj = find_card(current_level)

# #     if card_obj.get("submenu"):
# #         # Show submenu
# #         st.title(f"{card_obj['title']} Submenu")
# #         sub_cards = [{"title": s, "body": f"{s} report."} for s in card_obj["submenu"]]
# #         st.markdown(get_cards_html(sub_cards), unsafe_allow_html=True)
# #     else:
# #         # Final page
# #         st.title(f"{card_obj['title']} Page")

# #         # If this is activity report, call cont.main()
# #         if card_obj["title"].lower() == "activity":
# #             import cont  # make sure cont.py is in the same folder or in PYTHONPATH
# #             cont.main()  # call the function directly
# #         else:
# #             st.write(f"This is the detailed view for **{card_obj['title']}**.")

# #     # Back button always works
# #     if st.button("⬅ Back"):
# #         st.session_state.nav_stack.pop()  # go back
# #         st.rerun()

# # import streamlit as st

# # st.set_page_config(layout="wide", page_title="Responsive Cards Demo")


# # st.markdown("""
# # <style>
# # /* ---------- Container + Cards ---------- */
# # .cards-wrap {
# #   display: flex;
# #   gap: 12px;
# #   flex-wrap: wrap;
# #   padding: 8px 0;
# #   justify-content: flex-start; /* default for desktop */
# # }

# # .card {
# #   background: red;
# #   border-radius: 10px;
# #   box-shadow: 0 2px 10px rgba(0,0,0,0.06);
# #   padding: 16px;
# #   min-width: 160px;
# #   flex: 0 0 32%; /* desktop: ~3 per row */
# #   transition: transform 0.12s ease;
# #   overflow: hidden;
# # }

# # .card:hover { transform: translateY(-4px); }

# # .card h3 { margin:6px 0; font-size: clamp(16px,1.6vw,20px);}
# # .card p { margin:4px 0; font-size: clamp(13px,1.1vw,15px); color:#333; }

# # /* ---------- Responsive Breakpoints ---------- */

# # /* Tablet (≤992px) */
# # @media (max-width:992px){
# #   .card { flex: 0 0 32%; } /* 2 cards per row */
# # }

# # /* Phones (≤480px) */
# # @media (max-width:480px){
# #   .cards-wrap { justify-content: center } /* evenly distribute cards */
# #   .card { flex: 0 0 32%; padding: 10px; min-width: 140px; }
# #   .card h3 { font-size: 18px; }
# #   .card p { font-size: 15px; }
# # }

# # /* Tiny phones (≤350px) */
# # @media (max-width:350px){
# #   .cards-wrap { justify-content: space-around; }
# #   .card { flex: 0 0 48%; padding: 12px; min-width: 120px; }
# #   .card h3 { font-size: 15px; }
# #   .card p { font-size: 13px; }
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # # ---------- Cards data ----------
# # cards = [
# #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# #     {"title": "Archives", "body": "Browse archived documents and files."},
# #     {"title": "Team", "body": "Quick team stats and availability."}
# # ]

# # # ---------- Session State ----------
# # if "clicked_card" not in st.session_state:
# #     st.session_state.clicked_card = None

# # # Detect URL param
# # query_params = st.experimental_get_query_params()
# # if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
# #     st.session_state.clicked_card = query_params.get("nav")[0]

# # # ---------- Cache cards HTML ----------
# # @st.cache_data
# # def build_cards_html(clicked_card=None):
# #     html = '<div class="cards-wrap">'
# #     for c in cards:
# #         highlight = "border: 2px solid #4CAF50;" if clicked_card == c["title"].lower() else ""
# #         html += f'''<a href="/?nav={c["title"].lower()}" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# #             <div class="card" style="{highlight}">
# #                 <h3>{c["title"]}</h3>
# #                 <p>{c["body"]}</p>
# #             </div>
# #         </a>
# #         '''
# #     html += "</div>"
# #     return html

# # # ---------- Page Rendering ----------
# # if st.session_state.clicked_card is None:
# #     st.title("Responsive Cards Menu")
# #     st.markdown(build_cards_html(), unsafe_allow_html=True)
# # else:
# #     st.title(f"{st.session_state.clicked_card.title()} Page")
# #     st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

# #     # Only show the back button here
# #     if st.button("⬅ Back to Menu"):
# #         st.session_state.clicked_card = None
# #         st.experimental_set_query_params()
# #         st.rerun()

# # # import streamlit as st
# # # import pandas as pd

# # # st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # # # Optional: try to detect width using streamlit-js-eval (not required)
# # # try:
# # #     from streamlit_js_eval import streamlit_js_eval
# # #     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# # # except Exception:
# # #     width = None

# # # # ---------- Global CSS: container, cards, responsive table ----------
# # # st.markdown(
# # #     """
# # #     <style>
# # #     /* ---------- Container + Cards ---------- */
# # #     .cards-wrap {
# # #       display: flex;
# # #       gap: 12px;
# # #       align-items: flex-start;
# # #       justify-content: flex-start;
# # #       flex-wrap: wrap;               /* allow wrapping */
# # #       padding: 8px 0;
# # #       box-sizing: border-box;
# # #     }

# # #     .card {
# # #       background: #ffffff;
# # #       border-radius: 10px;
# # #       box-shadow: 0 2px 10px rgba(0,0,0,0.06);
# # #       padding: 16px;
# # #       min-width: 160px;             /* prevents cards from going too narrow */
# # #       flex: 0 0 32%;                /* desktop: ~3 per row */
# # #       box-sizing: border-box;
# # #       transition: transform 0.12s ease;
# # #       overflow: hidden;
# # #     }
# # #     .card:hover { transform: translateY(-4px); }
# # #     .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
# # #     .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

# # #     /* ---------- Table ---------- */
# # #     .resp-table { width:100%; border-collapse: collapse; margin-top: 8px; }
# # #     .resp-table th, .resp-table td { padding: 8px 10px; border: 1px solid #e6e6e6; text-align:left; font-size:14px; }
# # #     .resp-table th { background:#0d1b3d; color:#fff; }

# # #     /* ---------- Breakpoints ---------- */
# # #     /* Tablet-ish: 3->2 */
# # #     @media (max-width: 992px) {
# # #       .card { flex: 0 0 48%; }      /* 2 cards per row */
# # #     }

# # #     /* Phones: ensure 2 columns side-by-side down to 321px */
# # #     @media (max-width: 768px) {
# # #       .card { flex: 0 0 48%; padding: 12px; min-width: 140px; }
# # #       .cards-wrap { gap: 8px; }
# # #       .resp-table th, .resp-table td { font-size:13px; padding: 6px 8px; }
# # #     }

# # #     /* Very small phones but still bigger than tiny: keep 2 col behavior */
# # #     @media (max-width: 480px) {
# # #       .card { flex: 0 0 48%; padding: 10px; min-width: 120px; }
# # #       .card h3 { font-size: 14px; }
# # #       .card p { font-size: 12px; }
# # #       .resp-table th, .resp-table td { font-size:12px; }
# # #     }

# # #     /* TINY phones (<= 320px) -> fallback to single column */
# # #     @media (max-width: 320px) {
# # #       .card { flex: 0 0 100%; min-width: 100%; }
# # #       .cards-wrap { gap: 6px; }
# # #       .card h3 { font-size: 13px; }
# # #       .card p { font-size: 11px; }
# # #     }

# # #     /* ---------- Responsive table -> stacked rows on tiny screens ---------- */
# # #     @media (max-width: 480px) {
# # #       .resp-table, .resp-table thead, .resp-table tbody, .resp-table th, .resp-table td, .resp-table tr {
# # #         display: block;
# # #         width: 100%;
# # #       }
# # #       .resp-table thead { display: none; } /* hide table header on small screens */
# # #       .resp-table tr { margin-bottom: 12px; border: 1px solid #eee; padding: 8px; border-radius: 8px; box-shadow: 0 1px 4px rgba(0,0,0,0.03); }
# # #       .resp-table td { display: flex; justify-content: space-between; padding: 8px 10px; }
# # #       .resp-table td:before { content: attr(data-label); font-weight:600; margin-right:8px; color:#555; }
# # #     }
# # #     </style>
# # #     """,
# # #     unsafe_allow_html=True,
# # # )

# # # st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# # # # ---------- Dynamic rendering: use Streamlit native columns on large screens, custom container on smaller screens ----------
# # # LARGE_SCREEN_THRESHOLD = 992
# # # SMALL_SINGLE_COL_THRESHOLD = 320

# # # use_native_columns = False
# # # if width is not None:
# # #     st.write(f"📏 Detected browser width: {width}px")
# # #     if width >= LARGE_SCREEN_THRESHOLD:
# # #         use_native_columns = True
# # # else:
# # #     # width unknown: default to custom container (safe)
# # #     st.info("Screen width not detected — using responsive container (recommended).")

# # # # ------------- Option A: Streamlit native columns (desktop - optional) -------------
# # # if use_native_columns:
# # #     st.subheader("Native Streamlit columns (desktop)")
# # #     c1, c2, c3 = st.columns(3)
# # #     with c1:
# # #         st.metric("Metric A", "120")
# # #         st.write("Description A")
# # #     with c2:
# # #         st.metric("Metric B", "72")
# # #         st.write("Description B")
# # #     with c3:
# # #         st.metric("Metric C", "45")
# # #         st.write("Description C")
# # #     st.markdown("---")



# # # # # Cards data
# # # cards = [
# # #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# # #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# # #     {"title": "Archives", "body": "Browse archived documents and files."},
# # #     {"title": "Team", "body": "Quick team stats and availability."}
# # # ]

# # # # ---------- Detect clicked card ----------
# # # query_params = st.experimental_get_query_params()
# # # clicked_card = query_params.get("nav", [None])[0]

# # # # ---------- Page Routing ----------
# # # if not clicked_card:
# # #     # Show card menu
# # #     st.title("Responsive Cards Menu")
# # #     cards_html = '<div class="cards-wrap">'
# # #     for c in cards:
# # #         cards_html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# # #             <div class="card">
# # #                 <h3>{c["title"]}</h3>
# # #                 <p>{c["body"]}</p>
# # #             </div>
# # #         </a>
# # #         '''
# # #     cards_html += "</div>"
# # #     st.markdown(cards_html, unsafe_allow_html=True)

# # # else:
# # #     # Show detail page for the clicked card
# # #     st.title(f"{clicked_card.title()} Page")
# # #     st.write(f"This is the detailed view for **{clicked_card.title()}**.")
# # #     # Back link
# # #     st.markdown(
# # #         '<a href="/" target="_self" style="text-decoration:none; color:#4CAF50;">⬅ Back to Menu</a>',
# # #         unsafe_allow_html=True,
# # #     )
# # import streamlit as st
# # import pandas as pd

# # st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # # Optional: detect width
# # try:
# #     from streamlit_js_eval import streamlit_js_eval
# #     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# # except Exception:
# #     width = None

# # # ---------- Global CSS (unchanged) ----------
# # st.markdown("""
# # <style>
# # .cards-wrap {
# #   display: flex;
# #   gap: 12px;
# #   align-items: flex-start;
# #   justify-content: flex-start;
# #   flex-wrap: wrap;
# #   padding: 8px 0;
# #   box-sizing: border-box;
# # }
# # .card {
# #   background: #ffffff;
# #   border-radius: 10px;
# #   box-shadow: 0 2px 10px rgba(0,0,0,0.06);
# #   padding: 16px;
# #   min-width: 160px;
# #   flex: 0 0 32%;
# #   box-sizing: border-box;
# #   transition: transform 0.12s ease;
# #   overflow: hidden;
# # }
# # .card:hover { transform: translateY(-4px); }
# # .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
# # .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }
# # .resp-table { width:100%; border-collapse: collapse; margin-top: 8px; }
# # .resp-table th, .resp-table td { padding: 8px 10px; border: 1px solid #e6e6e6; text-align:left; font-size:14px; }
# # .resp-table th { background:#0d1b3d; color:#fff; }
# # @media (max-width: 992px) { .card { flex: 0 0 48%; } }
# # @media (max-width: 768px) { .card { flex: 0 0 48%; padding:12px; min-width:140px; } .cards-wrap { gap:8px; } .resp-table th, .resp-table td { font-size:13px; padding:6px 8px; } }
# # @media (max-width: 480px) { .card { flex: 0 0 48%; padding:10px; min-width:120px; } .card h3 { font-size:14px; } .card p { font-size:12px; } .resp-table th, .resp-table td { font-size:12px; } }
# # @media (max-width: 320px) { .card { flex:0 0 100%; min-width:100%; } .cards-wrap { gap:6px; } .card h3 { font-size:13px; } .card p { font-size:11px; } }
# # @media (max-width: 480px) {
# #     .resp-table, .resp-table thead, .resp-table tbody, .resp-table th, .resp-table td, .resp-table tr { display: block; width: 100%; }
# #     .resp-table thead { display: none; }
# #     .resp-table tr { margin-bottom: 12px; border: 1px solid #eee; padding:8px; border-radius:8px; box-shadow:0 1px 4px rgba(0,0,0,0.03);}
# #     .resp-table td { display: flex; justify-content: space-between; padding:8px 10px;}
# #     .resp-table td:before { content: attr(data-label); font-weight:600; margin-right:8px; color:#555; }
# # }
# # </style>
# # """, unsafe_allow_html=True)

# # # ---------- Screen width handling ----------
# # LARGE_SCREEN_THRESHOLD = 992
# # use_native_columns = False
# # if width is not None:
# #     st.write(f"📏 Detected browser width: {width}px")
# #     if width >= LARGE_SCREEN_THRESHOLD:
# #         use_native_columns = True
# # else:
# #     st.info("Screen width not detected — using responsive container.")

# # # ------------- Option A: Streamlit native columns (desktop) -------------
# # if use_native_columns:
# #     st.subheader("Native Streamlit columns (desktop)")
# #     c1, c2, c3 = st.columns(3)
# #     with c1:
# #         st.metric("Metric A", "120")
# #         st.write("Description A")
# #     with c2:
# #         st.metric("Metric B", "72")
# #         st.write("Description B")
# #     with c3:
# #         st.metric("Metric C", "45")
# #         st.write("Description C")
# #     st.markdown("---")

# # # ---------- Cards data ----------
# # cards = [
# #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# #     {"title": "Archives", "body": "Browse archived documents and files."},
# #     {"title": "Team", "body": "Quick team stats and availability."}
# # ]

# # # ---------- Session-state clicked card ----------
# # if "clicked_card" not in st.session_state:
# #     st.session_state.clicked_card = None

# # # ---------- Detect click via query param (only if no card selected yet) ----------
# # query_params = st.experimental_get_query_params()
# # if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
# #     st.session_state.clicked_card = query_params.get("nav")[0]

# # # ---------- Page rendering ----------
# # if st.session_state.clicked_card is None:
# #     # Show cards menu
# #     st.title("Responsive Cards Menu")

# #     cards_html = '<div class="cards-wrap">'
# #     for c in cards:
# #         cards_html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# #             <div class="card">
# #                 <h3>{c["title"]}</h3>
# #                 <p>{c["body"]}</p>
# #             </div>
# #         </a>
# #         '''
# #     cards_html += "</div>"
# #     st.markdown(cards_html, unsafe_allow_html=True)

# # else:
# #     # Show detail page
# #     st.title(f"{st.session_state.clicked_card.title()} Page")
# #     st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

# #     # Back button
# #     if st.button("⬅ Back to Menu"):
# #         st.session_state.clicked_card = None
# #         st.experimental_set_query_params()  # <- clears URL parameter so you can return
# #         st.rerun()


# import streamlit as st
# import pandas as pd

# st.set_page_config(layout="wide", page_title="Responsive Cards Demo")

# # Optional: detect width
# try:
#     from streamlit_js_eval import streamlit_js_eval
#     width = streamlit_js_eval(js_expressions="window.innerWidth", key="SCR_DETECT")
# except Exception:
#     width = None

# # ---------- Global CSS: container, cards, responsive table ----------
# st.markdown(
#     """
#     <style>
#     .cards-wrap {
#       display: flex;
#       gap: 12px;
#       align-items: flex-start;
#       justify-content: flex-start;
#       flex-wrap: wrap;
#       padding: 8px 0;
#       box-sizing: border-box;
#     }
#     .card {
#       background: #ffffff;
#       border-radius: 10px;
#       box-shadow: 0 2px 10px rgba(0,0,0,0.06);
#       padding: 16px;
#       min-width: 160px;
#       flex: 0 0 32%;
#       box-sizing: border-box;
#       transition: transform 0.12s ease;
#       overflow: hidden;
#     }
#     .card:hover { transform: translateY(-4px); }
#     .card h3 { margin: 6px 0; font-size: clamp(16px, 1.6vw, 20px); }
#     .card p { margin: 4px 0; font-size: clamp(13px, 1.1vw, 15px); color:#333; }

#     /* Table styling omitted for brevity (keep your original CSS) */

#     @media (max-width: 992px) { .card { flex: 0 0 48%; } }
#     @media (max-width: 768px) { .card { flex: 0 0 48%; padding: 12px; min-width: 140px; } }
#     @media (max-width: 480px) { .card { flex: 0 0 48%; padding: 10px; min-width: 120px; } }
#     @media (max-width: 320px) { .card { flex: 0 0 100%; min-width: 100%; } }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# st.title("Responsive Cards inside a Container (forces 2 columns on phones ≥321px)")

# # ---------- Dynamic rendering: large vs small screen ----------
# LARGE_SCREEN_THRESHOLD = 992
# use_native_columns = False
# if width is not None:
#     st.write(f"📏 Detected browser width: {width}px")
#     if width >= LARGE_SCREEN_THRESHOLD:
#         use_native_columns = True
# else:
#     st.info("Screen width not detected — using responsive container.")

# # ------------- Option A: Streamlit native columns (desktop) -------------
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

# # ---------- Cards data ----------
# # cards = [
# #     {"title": "Reports", "body": "Summary of the most recent reports and KPIs."},
# #     {"title": "Analytics", "body": "Interactive charts and trends overview."},
# #     {"title": "Archives", "body": "Browse archived documents and files."},
# #     {"title": "Team", "body": "Quick team stats and availability."}
# # ]

# # # ---------- Session-state clicked card ----------
# # if "clicked_card" not in st.session_state:
# #     st.session_state.clicked_card = None

# # # Only update clicked_card if session_state is empty
# # query_params = st.experimental_get_query_params()
# # if query_params.get("nav", [None])[0] and st.session_state.clicked_card is None:
# #     st.session_state.clicked_card = query_params.get("nav")[0]

# # # ---------- Memoized function to build cards HTML ----------
# # # ---------- Memoized function to build cards HTML ----------
# # @st.cache_data
# # def get_cards_html(clicked=None):
# #     html = '<div class="cards-wrap">'
# #     for c in cards:
# #         highlight_style = "border: 2px solid #4CAF50;" if clicked == c["title"].lower() else ""
# #         html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
# #             <div class="card" style="{highlight_style}">
# #                 <h3>{c["title"]}</h3>
# #                 <p>{c["body"]}</p>
# #             </div>
# #         </a>
# #         '''
# #     html += "</div>"
# #     return html

# # # ---------- Page rendering ----------
# # if st.session_state.clicked_card is None:
# #     # Show cards menu
# #     st.title("Responsive Cards Menu")
# #     st.markdown(get_cards_html(), unsafe_allow_html=True)
# # else:
# #     # Show detailed card page
# #     st.title(f"{st.session_state.clicked_card.title()} Page")
# #     st.write(f"This is the detailed view for **{st.session_state.clicked_card.title()}**.")

# #     # Back button
# #     if st.button("⬅ Back to Menu"):
# #         st.session_state.clicked_card = None
# #         st.experimental_set_query_params()  # clear URL
# #         st.rerun()
# # #


# import streamlit as st

# # ---------- Cards & submenus ----------
# cards = [
#     {"title": "Reports", "body": "Summary of recent reports.", "submenu": ["Financial", "Activity"]},
#     {"title": "Analytics", "body": "Interactive charts.", "submenu": []},
#     {"title": "Archives", "body": "Browse archived documents.", "submenu": []},
#     {"title": "Team", "body": "Quick team stats.", "submenu": []}
# ]

# # ---------- Session state ----------
# if "nav_stack" not in st.session_state:
#     st.session_state.nav_stack = []  # navigation history

# # ---------- Handle card clicks ----------
# query_params = st.experimental_get_query_params()
# clicked = query_params.get("nav", [None])[0]

# if clicked:
#     st.session_state.nav_stack.append(clicked)
#     st.experimental_set_query_params()  # clear query param
#     st.rerun()

# # ---------- Current level ----------
# current_level = st.session_state.nav_stack[-1] if st.session_state.nav_stack else None

# # ---------- Global CSS ----------
# st.markdown("""
# <style>
# .cards-wrap { display: flex; gap: 12px; flex-wrap: wrap; padding:8px 0; justify-content:flex-start; }
# .card { background:#fff; border-radius:10px; box-shadow:0 2px 10px rgba(0,0,0,0.06); padding:16px; min-width:160px; flex:0 0 32%; transition: transform 0.12s ease; overflow:hidden; }
# .card:hover { transform: translateY(-4px); }
# .card h3 { margin:6px 0; font-size:clamp(16px,1.6vw,20px); }
# .card p { margin:4px 0; font-size:clamp(13px,1.1vw,15px); color:#333; }
# @media (max-width:992px){ .card{ flex:0 0 48%; } }
# @media (max-width:480px){ .cards-wrap{ justify-content: space-around; } .card{ flex:0 0 48%; padding:14px; min-width:140px;} .card h3{ font-size:16px;} .card p{ font-size:14px; } }
# @media (max-width:350px){ .cards-wrap{ justify-content: space-around; } .card{ flex:0 0 48%; padding:12px; min-width:120px;} .card h3{ font-size:15px;} .card p{ font-size:13px; } }
# </style>
# """, unsafe_allow_html=True)

# # ---------- Memoized HTML ----------
# @st.cache_data
# def get_cards_html(cards_list):
#     html = '<div class="cards-wrap">'
#     for c in cards_list:
#         html += f'''<a href="/?nav={c["title"].lower()}" target="_self" style="text-decoration:none; color:inherit; flex:0 0 32%;">
#             <div class="card">
#                 <h3>{c["title"]}</h3>
#                 <p>{c.get("body","")}</p>
#             </div>
#         </a>'''
#     html += "</div>"
#     return html
# import os
# import base64

# img_path = os.path.join("paul.jpg")

# # Encode image to base64
# with open(img_path, "rb") as f:
#     img_bytes = f.read()
# img_b64 = base64.b64encode(img_bytes).decode()

# # ---------- Helper to find card ----------
# def find_card(title):
#     for c in cards:
#         if c["title"].lower() == title:
#             return c
#         if "submenu" in c and title in [s.lower() for s in c["submenu"]]:
#             return {"title": title, "body": f"{title.title()} report.", "submenu": []}
#     return None

# # ---------- Page rendering ----------
# # if not current_level:
# #     # Main menu
# #     st.title("Main Menu")
# #     st.markdown(get_cards_html(cards), unsafe_allow_html=True)
# # else:
# #     card_obj = find_card(current_level)

# #     if card_obj.get("submenu"):
# #         # Show submenu
# #         st.title(f"{card_obj['title']} Submenu")
# #         sub_cards = [{"title": s, "body": f"{s} report."} for s in card_obj["submenu"]]
# #         st.markdown(get_cards_html(sub_cards), unsafe_allow_html=True)
# #     else:
# #         # Final page
# #         st.title(f"{card_obj['title']} Page")
# #         st.write(f"This is the detailed view for **{card_obj['title']}**.")

# #     # Back button always works
# #     if st.button("⬅ Back"):
# #         st.session_state.nav_stack.pop()  # go back
# #         st.rerun()
# # if not current_level:
#     # Main menu
#     # st.title("Main Menu")
#     # st.markdown(get_cards_html(cards), unsafe_allow_html=True)
#     # if not current_level:
#     # Main menu
#     # st.title("Main Menu")

#     # ---------- Introductory image ----------
#     # st.image("paul.jpg", use_column_width=True)  # responsive width

#     # Display cards
#     # st.markdown(get_cards_html(cards), unsafe_allow_html=True)
# if not current_level:
# #     # Path to image
# #     img_path = os.path.join("images", "std.jpg")

# #     # Encode image to base64
# #     with open(img_path, "rb") as f:
# #         img_bytes = f.read()
# #     img_b64 = base64.b64encode(img_bytes).decode()

# #     # Inject CSS with image as background
# #     st.markdown(f"""
# #     <style>
# #     .intro-img {{
# #         background-image: url("data:image/jpg;base64,{img_b64}");
# #         background-size: cover;
# #         background-position: center;
# #         width: 50%;
# #         height: px;  /* desktop height */
# #         border-radius: 10px;
# #         margin-bottom: 20px;
# #     }}
# #     @media (max-width:480px) {{
# #         .intro-img {{
# #             height: 180px;  /* mobile height */
# #         }}
# #     }}
# #     </style>

# #     <div class="intro-img"></div>
# #     """, unsafe_allow_html=True)

# #         # Display cards
# #     st.markdown(get_cards_html(cards), unsafe_allow_html=True)


# # CSS with controlled position
#     # st.markdown(f"""
#     # <style>
#     # .intro-img {{
#     #     background-image: url("data:image/jpg;base64,{img_b64}");
#     #     background-size: cover;
#     #     background-position: center;
#     #     width: 200px;       /* width of the image */
#     #     height: 150px;      /* height of the image */
#     #     border-radius: 10px;
#     #     position: absolute; /* absolute positioning */
#     #     top: 10px;          /* distance from top */
#     #     right: 10px;        /* distance from right */
#     #     box-shadow: 0 2px 10px rgba(0,0,0,0.2);
#     # }}
#     # @media (max-width:480px) {{
#     #     .intro-img {{
#     #         width: 300px;
#     #         height: 100px;
#     #         top: 0px;
#     #         right: 20px;
#     #     }}
#     # }}
#     # </style>

#     # <div class="intro-img"></div>
#     # """, unsafe_allow_html=True)
#     st.markdown(f"""
#     <style>
#     .top-banner {{
#         display: flex;
#         flex-wrap: wrap;
#         gap: 16px;
#         background: #f8f9fa;
#         border-radius: 12px;
#         padding: 16px;
#         align-items: center;
#         margin-bottom: 24px;
#     }}
#     .banner-img {{
#         flex: 0 0 40%;
#         max-width: 40%;
#         border-radius: 10px;
#         box-shadow: 0 2px 10px rgba(0,0,0,0.1);
#         background-image: url("data:image/jpg;base64,{img_b64}");
#         background-size: cover;
#         background-position: center;
#         height: 200px;
#     }}
#     .banner-text {{
#         flex: 1;
#         font-family: Arial, sans-serif;
#         color: #333;
#         padding: 8px 16px;
#     }}
#     @media (max-width: 768px) {{
#         .banner-img, .banner-text {{
#             flex: 0 0 100%;
#             max-width: 100%;
#             height: 180px;
#         }}
#         .banner-text {{
#             padding: 8px 0;
#         }}
#     }}
#     </style>

#     <div class="top-banner">
#         <div class="banner-img"></div>
#         <div class="banner-text">
#             <h2>Welcome to the Dashboard</h2>
#             <p>This is your introductory image and description section. It adjusts perfectly on PC and mobile screens, keeping the layout clean and readable.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(get_cards_html(cards), unsafe_allow_html=True)


# else:
#     card_obj = find_card(current_level)

#     if card_obj.get("submenu"):
#         # Show submenu
#         st.title(f"{card_obj['title']} Submenu")
#         sub_cards = [{"title": s, "body": f"{s} report."} for s in card_obj["submenu"]]
#         st.markdown(get_cards_html(sub_cards), unsafe_allow_html=True)
#     else:
#         # Final page
#         st.title(f"{card_obj['title']} Page")

#         # If this is activity report, call cont.main()
#         if card_obj["title"].lower() == "activity":
#             import cont  # make sure cont.py is in the same folder or in PYTHONPATH
#             cont.main()  # call the function directly
#         else:
#             st.write(f"This is the detailed view for **{card_obj['title']}**.")

#     # Back button always works
#     if st.button("⬅ Back"):
#         st.session_state.nav_stack.pop()  # go back
#         st.rerun()

import streamlit as st
import base64

st.set_page_config(page_title="News Card", layout="wide")

IMAGE_PATH = "/mnt/data/a77ab8be-0bc3-4608-b601-b1ed8226bf5c.jpg"

def get_base64_of_image(image_file: str) -> str:
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64_of_image(IMAGE_PATH)

# Font Awesome CDN
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)

# CSS Styling
st.markdown(
    f"""
    <style>
    /* Top header / logo bar */
    .topbar {{
        display:flex;
        align-items:center;
        justify-content:space-between;
        background: white;
        padding: 12px 18px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        border-radius: 8px;
        margin-bottom: 16px;
        flex-wrap: wrap;
    }}
    .logo {{
        display:flex;
        align-items:center;
        gap:10px;
    }}
    .logo-icon {{
        font-size:34px;
        color:#1e40af;
    }}
    .logo-text .logo-main {{
        font-size:22px;
        font-weight:700;
        color:#1e40af;
        line-height:1;
    }}
    .logo-text .logo-sub {{
        display:block;
        font-size:12px;
        color: #8b8b8b;
        margin-top:2px;
    }}

    /* Header buttons */
    .header-buttons {{
        display:flex;
        gap:12px;
    }}
    .header-buttons a {{
        padding:8px 16px;
        border-radius:6px;
        text-decoration:none;
        font-size:14px;
        font-weight:600;
        transition: background 0.25s ease;
    }}
    .btn-signin {{
        background:#2563eb;
        color:white;
    }}
    .btn-signin:hover {{
        background:#1e40af;
    }}
    .btn-help {{
        background:#f3f4f6;
        color:#111827;
    }}
    .btn-help:hover {{
        background:#e5e7eb;
    }}

    /* Hero card */
    .news-card {{
        position: relative;
        width: 100%;
        height: 420px;
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        border-radius: 10px;
        overflow: hidden;
    }}
    .news-card:before {{
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(0,0,0,0.42) 10%, rgba(0,0,0,0.62) 65%);
        z-index: 0;
    }}
    .overlay-text {{
        position: relative;
        z-index: 2;
        padding: 28px;
        color: white;
        display:flex;
        flex-direction:column;
        align-items:center;
        text-align:center;
        gap:12px;
    }}
    .overlay-text h1 {{
        margin:0;
        font-size:34px;
        font-weight:700;
        line-height:1.05;
        max-width:900px;
    }}

    .meta-row {{
        display:flex;
        gap:12px;
        align-items:center;
        flex-wrap:wrap;
        justify-content:center;
    }}
    .tags span {{
        display:inline-block;
        background:#2563eb;
        color:white;
        padding:6px 12px;
        border-radius:999px;
        font-size:13px;
    }}
    .date {{
        color: #d1d5db;
        font-size:14px;
    }}

    /* Social icons */
    .social-icons {{
        display:flex;
        gap:10px;
        align-items:center;
        margin-top:6px;
    }}
    .social-icons a {{
        display:inline-flex;
        width:44px;
        height:44px;
        border-radius:50%;
        align-items:center;
        justify-content:center;
        color:white;
        text-decoration:none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.18);
        transition: transform .12s ease;
    }}
    .social-icons a:hover {{ transform: translateY(-3px); }}
    .social-icons .fb {{ background:#1877F2; }}
    .social-icons .x  {{ background:#1DA1F2; }}
    .social-icons .li {{ background:#0A66C2; }}
    .social-icons .rd {{ background:#FF4500; }}

    .caption {{
        font-size:13px;
        color: #6b7280;
        margin-top:10px;
    }}
    .summary {{
        background:white;
        color:#111827;
        padding:22px;
        border-radius:10px;
        margin-top:18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}

    /* Responsive tweaks */
    @media (max-width: 700px) {{
        .news-card {{ height: 360px; }}
        .overlay-text h1 {{ font-size:20px; }}
        .logo-text .logo-main {{ font-size:18px; }}
        .header-buttons {{
            width:100%;
            justify-content:flex-end;
            margin-top:8px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML Content
st.markdown(
    """
    <div class="topbar">
        <div class="logo">
            <i class="fas fa-brain logo-icon" aria-hidden="true"></i>
            <div class="logo-text">
                <span class="logo-main">Neuroscience</span>
                <span class="logo-sub">News.com</span>
            </div>
        </div>
        <div class="header-buttons">
            <a href="#" class="btn-signin">Sign In</a>
            <a href="#" class="btn-help">Help</a>
        </div>
    </div>

    <div class="news-card">
        <div class="overlay-text">
            <h1>Opioid Use in Pregnancy Not Linked to Autism or ADHD Risk</h1>
            <div class="meta-row">
                <div class="tags">
                    <span>Autism</span>
                    <span>Featured</span>
                    <span>Neuroscience</span>
                </div>
                <div class="date">September 16, 2025</div>
            </div>
            <div class="social-icons">
                <a class="fb" href="https://facebook.com" target="_blank"><i class="fab fa-facebook-f"></i></a>
                <a class="x" href="https://twitter.com" target="_blank"><i class="fab fa-x-twitter"></i></a>
                <a class="li" href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                <a class="rd" href="https://reddit.com" target="_blank"><i class="fab fa-reddit-alien"></i></a>
            </div>
        </div>
    </div>

    <div class="caption">
        Similarly, the risk for these neurodevelopmental conditions disappeared when comparing differentially exposed siblings. Credit: Neuroscience News.
    </div>

    <div class="summary">
        <b>Summary:</b> A large-scale study analyzing over a million births in Sweden found no evidence that prescribed opioid pain medications during pregnancy cause autism or ADHD in children. While earlier data raised concerns, this study provides strong evidence to the contrary.
    </div>
    """,
    unsafe_allow_html=True,
)



















