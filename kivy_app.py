import streamlit as st
import streamlit.components.v1 as components

st.title("Circular Story with Arrows Inside Container")
st.write("Items appear sequentially around a circle, arrows now visible inside container.")

components.html("""
<style>
#circle-container {
    position: relative;
    width: 400px;
    height: 400px;
    margin: auto;
    border-radius: 50%;
    background: #f5f5f5;
}
.floating-story {
    position: absolute;
    background-color: #ff6600;
    color: white;
    padding: 10px 15px;
    border-radius: 12px;
    font-size: 16px;
    opacity: 0;
    transition: opacity 0.5s ease-in-out, transform 0.5s ease-in-out;
    text-align: center;
    cursor: pointer;
    max-width: 150px;
}
.floating-story.show {
    opacity: 1;
}
.floating-story img {
    max-width: 100%;
    height: auto;
    display: block;
    border-radius: 8px;
}
.arrow {
    position: absolute;
    top: 50%;
    font-size: 32px;
    cursor: pointer;
    user-select: none;
    color: #333;
    transform: translateY(-50%);
}
.arrow.left { left: -50px; }
.arrow.right { right: -50px; }
</style>

<div id="circle-container">
    <div class="arrow left">&#8592;</div>
    <div class="arrow right">&#8594;</div>
</div>

<script>
const storyContent = [
    {type: 'text', content: '💬 Hi! Talk to us'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1503023345310-bd7c1de61c7d?&w=150'},
    {type: 'image', content: 'https://images.unsplash.com/photo-1506744038136-46273834b3fb?&w=150'},
    {type: 'text', content: '🌞 Enjoy your day!'},
    {type: 'text', content: 'Short text'},
    {type: 'text', content: 'A longer sentence to test size'}
];

const container = document.getElementById('circle-container');
const durationPerItem = 1000;
const pauseAfterAll = 5000;
const radius = 150;
let currentIndex = 0;
let divs = [];

function createCircle() {
    // Remove previous items
    divs.forEach(d=>d.remove());
    divs = [];
    const n = storyContent.length;
    const centerX = container.clientWidth/2;
    const centerY = container.clientHeight/2;

    storyContent.forEach((item,i)=>{
        const div = document.createElement('div');
        div.className='floating-story';
        const angle = 2*Math.PI*i/n;
        const x = centerX + radius * Math.cos(angle) - 75;
        const y = centerY + radius * Math.sin(angle) - 25;
        div.style.left = x+'px';
        div.style.top = y+'px';
        if(item.type==='text'){
            div.innerHTML=item.content;
        } else {
            div.innerHTML=`<img src="${item.content}">`;
        }
        div.onclick=()=>window.open('https://example.com','_blank');
        container.appendChild(div);
        divs.push(div);
    });
}

// Sequentially show one by one
function showStory() {
    divs.forEach(div=>div.classList.remove('show'));
    for(let i=0;i<divs.length;i++){
        setTimeout(()=>divs[i].classList.add('show'), i*durationPerItem);
    }
    setTimeout(()=>divs.forEach(div=>div.classList.remove('show')), divs.length*durationPerItem + pauseAfterAll);
}

// Manual navigation
function navigate(offset){
    if(divs.length===0) return;
    currentIndex = (currentIndex + offset + divs.length)%divs.length;
    divs.forEach(div=>div.classList.remove('show'));
    divs[currentIndex].classList.add('show');
}

document.querySelector('.arrow.left').onclick=()=>navigate(-1);
document.querySelector('.arrow.right').onclick=()=>navigate(1);

createCircle();
showStory();
setInterval(showStory, divs.length*durationPerItem + pauseAfterAll + 1000);
</script>
""", height=500)
