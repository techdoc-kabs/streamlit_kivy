import streamlit as st
import streamlit.components.v1 as components

st.title("Floating Animated Notification Example")
st.write("This simulates an in-page animated notification or banner.")

# HTML + CSS + JS for a floating notification
components.html("""
<style>
#floating-notice {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #00aaff;
    color: white;
    padding: 15px 20px;
    border-radius: 10px;
    font-size: 16px;
    z-index: 9999;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    opacity: 0;
    transform: translateX(100%);
    transition: all 0.5s ease-in-out;
    cursor: pointer;
}
#floating-notice.show {
    opacity: 1;
    transform: translateX(0);
}
</style>

<div id="floating-notice" onclick="window.open('https://example.com','_blank')">
    💬 Hi! Talk to us
</div>

<script>
function showNotice(){
    const notice = document.getElementById('floating-notice');
    notice.classList.add('show');  // slide in
    setTimeout(() => {
        notice.classList.remove('show');  // slide out after 3s
    }, 3000);
}

// Show every 5 seconds
setInterval(showNotice, 5000);
</script>
""", height=0)
