import streamlit as st

# Define menus
MENUS = {
    "main": ["Consultations", "Reports", "Files", "Schedules"],
    "Consultations": ["New Session", "History"],
    "Schedules": ["Upcoming", "Past"]
}

# --- Navigation via query params ---
query = st.query_params.get("page", ["main"])[0]

if "back" in st.query_params:
    for parent, submenu in MENUS.items():
        if query in submenu:
            st.query_params["page"] = parent
            st.rerun()
    st.query_params["page"] = "main"
    st.rerun()

current_page = query

# --- Back Button ---
if current_page != "main":
    st.markdown(
        f"""
        <button onclick="window.location.href='/?back=1'" 
        style="padding:10px 15px; border:none; background:#555; color:white; border-radius:6px;">
            ⬅ Back
        </button>
        """,
        unsafe_allow_html=True
    )

st.write(f"### {current_page}")

# --- Two-column card layout ---
html = "<table style='width:100%; text-align:center;'>"
buttons = MENUS[current_page]
for i in range(0, len(buttons), 2):
    html += "<tr>"
    for item in buttons[i:i+2]:
        html += f"""<td style='padding:8px;'>
            <button onclick="window.location.href='/?page={item}'"
                style="
                    background:#3498db; 
                    color:white;
                    padding:14px;
                    border:none;
                    border-radius:8px;
                    width:100%;
                    font-size:16px;
                    cursor:pointer;
                ">{item}</button>
        </td>
        """
    html += "</tr>"
html += "</table>"

st.markdown(html, unsafe_allow_html=True)
