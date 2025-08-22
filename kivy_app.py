import streamlit as st
import streamlit.components.v1 as components

def auto_toast_with_action(
    message,
    icon="info",
    interval=5000,
    duration=3000,
    position="top-end",
    action_text="👉 Click me",
    action_url="#"
):
    """
    Display an automatic repeating toast with an interactive action.
    
    Args:
        message (str): Main toast message.
        icon (str): 'info', 'success', 'warning', 'error'.
        interval (int): Time between each toast in milliseconds.
        duration (int): Toast visibility duration in milliseconds.
        position (str): Toast position: 'top-end', 'top-start', 'bottom-end', 'bottom-start'.
        action_text (str): Text or emoji for the clickable action.
        action_url (str): URL or JS link triggered by clicking the action.
    """
    toast_html = f"""
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script>
    function showToast() {{
        const Toast = Swal.mixin({{
            toast: true,
            position: '{position}',
            showConfirmButton: false,
            timer: {duration},
            timerProgressBar: true,
            html: `{message} <a href='{action_url}' target='_blank' style='text-decoration:none; margin-left:10px;'>{action_text}</a>`
        }});
        Toast.fire({{
            icon: '{icon}'
        }});
    }}
    setInterval(showToast, {interval});
    </script>
    """
    components.html(toast_html, height=0)

# --- Example Usage ---
st.title("Interactive Auto Toast")
st.write("This toast repeats automatically and includes a clickable emoji.")

auto_toast_with_action(
    message="Hi! Talk to us",
    icon="info",
    interval=5000,
    duration=3000,
    action_text="💬",
    action_url="https://example.com/chat"
)
