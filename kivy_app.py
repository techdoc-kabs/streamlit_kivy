import streamlit as st
import streamlit.components.v1 as components

st.title("Sequential Floating Story - Full Vertical Space")
st.write("Items appear one by one, use more vertical space, then disappear together.")

components.html("""
<style>
#story-container {
    position: fixed;
    bottom: 20px;
    right: 20px;
    display: flex;
    flex-direction: column-reverse; /* newest at bottom */
    align-items: flex-end;
    max-height: 80vh;  /* use most of the vertical viewport */
    overflow: hidden;
    z-index: 9999;
}

.floating-story {
    background-color: #ff6600;
    color: white;
    padding: 10px 15px;
    border-radius: 12px;
    font-size: 16px;
    margin-top: 10px;
    opacity: 0;
    transition: all 0.5s ease-in-out;
    max-width: 250px;
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

function showStackedStory() {
    const container = document.getElementById('story-container');
    container.innerHTML = ''; // clear previous

    const divs = [];

    storyContent.forEach((item, i) => {
        const div = document.createElement('div');
        div.className = 'floating-story';
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
