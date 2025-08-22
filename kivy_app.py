import streamlit as st
import streamlit.components.v1 as components

st.title("Sequential Horizontal Story")
st.write("Items flow horizontally, appear one by one, then disappear together.")

components.html("""
<style>
#story-container {
    display: flex;
    flex-wrap: wrap;  /* allows items to flow to next line */
    justify-content: center; /* center horizontally */
    gap: 20px; /* spacing between items */
    margin-top: 50px;
}
.floating-story {
    background-color: #ff6600;
    color: white;
    padding: 10px 15px;
    border-radius: 12px;
    font-size: 16px;
    opacity: 0;
    transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    max-width: 150px;
    text-align: center;
    cursor: pointer;
}
.floating-story.show {
    opacity: 1;
    transform: translateY(0);
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
    {type: 'image', content: 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?&w=150'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?&w=150'},
    {type: 'text', content: '🌞 Enjoy your day!'}
];

const durationPerItem = 1000; // 1 sec per item
const pauseAfterAll = 2000;   // 2 sec pause after all appear

function showFlowingStory() {
    const container = document.getElementById('story-container');
    container.innerHTML = '';
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
    setTimeout(() => {
        divs.forEach(div => div.classList.remove('show'));
        setTimeout(() => divs.forEach(div => div.remove()), 500);
    }, divs.length * durationPerItem + pauseAfterAll);
}

// start immediately and repeat
showFlowingStory();
setInterval(showFlowingStory, storyContent.length * durationPerItem + pauseAfterAll + 1000);
</script>
""", height=300)
