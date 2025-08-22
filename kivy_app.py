import streamlit as st
import streamlit.components.v1 as components

st.title("Sequential Floating Story - Non-Overlapping")
st.write("Items appear one by one, stacked above each other, then all disappear together.")

components.html("""
<style>
.floating-story {
    position: fixed;
    right: 20px;
    background-color: #ff6600;
    color: white;
    padding: 10px 15px;
    border-radius: 12px;
    font-size: 16px;
    z-index: 9999;
    box-shadow: 0 4px 6px rgba(0,0,0,0.3);
    opacity: 0;
    transition: all 0.5s ease-in-out;
    max-width: 220px;
    text-align: center;
    cursor: pointer;
}
.floating-story.show {
    opacity: 1;
}
.floating-story img {
    max-width: 100%;
    border-radius: 8px;
}
</style>

<div id="story-container"></div>

<script>
const storyContent = [
    {type: 'text', content: '💬 Hi! Talk to us'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?&w=200'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?&w=200'},
    {type: 'text', content: '🌞 Enjoy your day!'}
];

const durationPerItem = 1000; // 1 sec per item
const pauseAfterAll = 2000;   // 2 sec pause after all appear
const spacing = 80;           // vertical spacing between items in px

function showStackedStory() {
    const container = document.getElementById('story-container');
    container.innerHTML = ''; // clear previous

    const divs = [];

    storyContent.forEach((item, i) => {
        const div = document.createElement('div');
        div.className = 'floating-story';
        div.style.bottom = (20 + i * spacing) + 'px'; // dynamic vertical position
        if(item.type === 'text'){
            div.innerHTML = item.content;
        } else if(item.type === 'image'){
            div.innerHTML = `<img src="${item.content}">`;
        }
        div.onclick = () => window.open('https://example.com','_blank');
        container.appendChild(div);
        divs.push(div);
    });

    // sequentially show items
    divs.forEach((div, i) => {
        setTimeout(() => div.classList.add('show'), i * durationPerItem);
    });

    // hide all at once
    setTimeout(() => divs.forEach(div => div.classList.remove('show')), divs.length * durationPerItem + pauseAfterAll);
}

// start immediately and repeat
showStackedStory();
setInterval(showStackedStory, storyContent.length * durationPerItem + pauseAfterAll + 1000);
</script>
""", height=0)
