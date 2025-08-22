import streamlit as st
import streamlit.components.v1 as components

def sweet_alert(title, message, icon="info", timer=None):
    timer_code = f"timer: {timer}," if timer else ""
    html_code = f"""
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script>
      Swal.fire({{
        title: '{title}',
        text: '{message}',
        icon: '{icon}',
        {timer_code}
        confirmButtonText: 'OK'
      }});
    </script>
    """
    components.html(html_code, height=0, width=0)

# Buttons to test
if st.button("Show Success"):
    sweet_alert("Done!", "Your data was saved successfully.", "success")

if st.button("Show Auto Close"):
    sweet_alert("Auto Close", "This will close in 2 sec.", "info", timer=2000)
