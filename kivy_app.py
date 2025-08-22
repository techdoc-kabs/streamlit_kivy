import streamlit as st
import streamlit.components.v1 as components

st.title("Floating Full-Story Carousel")
st.write("Displays the full story sequence at once, then disappears, then repeats.")

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
    {type: 'image', content: 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?&w=200'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?&w=200'},
    {type: 'text', content: '🌞 Enjoy your day!'}
];

function showFullStory() {
    const notice = document.getElementById('story-notice');
    // Build full HTML
    let html = '';
    for (let i=0; i<storyContent.length; i++){
        if(storyContent[i].type === 'text'){
            html += '<div>' + storyContent[i].content + '</div>';
        } else if(storyContent[i].type === 'image'){
            html += '<img src="' + storyContent[i].content + '">';
        }
    }
    notice.innerHTML = html;
    notice.classList.add('show');  // show full story

    // Hide after story duration
    setTimeout(() => notice.classList.remove('show'), 3000 * storyContent.length);
}

// Repeat every (story_length * duration + pause) milliseconds
setInterval(showFullStory, 5000 + (3000 * storyContent.length));

</script>
""", height=0)
