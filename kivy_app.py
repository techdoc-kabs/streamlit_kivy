import streamlit as st
import streamlit.components.v1 as components

# SweetAlert2 toast loader
toast_html = """
<script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
<script>
function showToast() {
    const Toast = Swal.mixin({
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      timer: 3000,
      timerProgressBar: true
    });
    Toast.fire({
      icon: 'info',
      title: 'Hi! Talk to us'
    });
}

// Show toast every 5 seconds
setInterval(showToast, 5000);
</script>
"""

# Inject into Streamlit
components.html(toast_html, height=0)
st.title("Automatic Toast Example")
st.write("This will show a toast notification every 5 seconds.")
