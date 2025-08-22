import streamlit as st
from streamlit_javascript import st_javascript

# Load SweetAlert2 once
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
""", unsafe_allow_html=True)

def sweet_alert(title, message, icon="info", timer=None):
    """
    Show a SweetAlert2 popup in Streamlit.
    
    Args:
        title (str): Title of the popup.
        message (str): Message/body text.
        icon (str): 'success', 'error', 'warning', 'info', 'question'
        timer (int): Auto-close time in ms (optional)
    """
    timer_code = f"timer: {timer}," if timer else ""
    st_javascript(f"""
    () => {{
        Swal.fire({{
          title: '{title}',
          text: '{message}',
          icon: '{icon}',
          {timer_code}
          confirmButtonText: 'OK'
        }});
    }}
    """)

# Example usage
if st.button("Show Success Alert"):
    sweet_alert("Done!", "Your data was saved successfully.", "success")

if st.button("Show Auto-close Alert"):
    sweet_alert("Auto Close", "This will close in 2 sec.", "info", timer=2000)
