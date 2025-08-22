import streamlit as st
import streamlit.components.v1 as components

st.title("Floating Story Carousel Example")
st.write("A floating notification that cycles through text and images like a story.")

# HTML + CSS + JS for story carousel
components.html("""
<style>
#story-notice {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #ff6600;
    color: white;
    padding: 15px 20px;
    border-radius: 12px;
    font-size: 16px;
    z-index: 9999;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    opacity: 0;
    transform: translateX(100%);
    transition: all 0.5s ease-in-out;
    max-width: 250px;
    text-align: center;
    cursor: pointer;
}
#story-notice.show {
    opacity: 1;
    transform: translateX(0);
}
#story-notice img {
    max-width: 100%;
    border-radius: 8px;
    margin-top: 5px;
}
</style>

<div id="story-notice" onclick="window.open('https://example.com','_blank')"></div>

<script>
const storyContent = [
    {type: 'text', content: '💬 Hi! Talk to us'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?&w=200'},  // example image
    {type: 'image', content: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?&w=200'},  // example sun/dog
    {type: 'text', content: '🌞 Enjoy your day!'}
];

let index = 0;

function showStory() {
    const notice = document.getElementById('story-notice');
    const current = storyContent[index];
    
    if(current.type === 'text') {
        notice.innerHTML = current.content;
    } else if(current.type === 'image') {
        notice.innerHTML = `<img src='${current.content}'>`;
    }
    
    notice.classList.add('show');  // slide in
    setTimeout(() => notice.classList.remove('show'), 3000);  // slide out after 3s
    
    index = (index + 1) % storyContent.length;
}

// Repeat every 5 seconds
setInterval(showStory, 5000);
</script>
""", height=0)
