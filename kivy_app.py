import streamlit as st
import base64

st.set_page_config(page_title="News Card", layout="wide")

# IMAGE_PATH = "images/std.jpg"
IMAGE_PATH = "paul.jpg"

def get_base64_of_image(image_file: str) -> str:
    with open(image_file, "rb") as f:
        return base64.b64encode(f.read()).decode()

img_base64 = get_base64_of_image(IMAGE_PATH)

# Font Awesome CDN
st.markdown(
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">',
    unsafe_allow_html=True,
)

# CSS Styling
st.markdown(
    f"""
    <style>
    /* Top header / logo bar */
    .topbar {{
        display:flex;
        align-items:center;
        justify-content:space-between;
        background: white;
        padding: 12px 18px;
        box-shadow: 0 2px 6px rgba(0,0,0,0.08);
        border-radius: 8px;
        margin-bottom: 16px;
        flex-wrap: wrap;
    }}
    .logo {{
        display:flex;
        align-items:center;
        gap:10px;
    }}
    .logo-icon {{
        font-size:34px;
        color:#1e40af;
    }}
    .logo-text .logo-main {{
        font-size:22px;
        font-weight:700;
        color:#1e40af;
        line-height:1;
    }}
    .logo-text .logo-sub {{
        display:block;
        font-size:12px;
        color: #8b8b8b;
        margin-top:2px;
    }}

    /* Header buttons */
    .header-buttons {{
        display:flex;
        gap:12px;
    }}
    .header-buttons a {{
        padding:8px 16px;
        border-radius:6px;
        text-decoration:none;
        font-size:14px;
        font-weight:600;
        transition: background 0.25s ease;
    }}
    .btn-signin {{
        background:#2563eb;
        color:white;
    }}
    .btn-signin:hover {{
        background:#1e40af;
    }}
    .btn-help {{
        background:#f3f4f6;
        color:#111827;
    }}
    .btn-help:hover {{
        background:#e5e7eb;
    }}

    /* Hero card */
    .news-card {{
        position: relative;
        width: 100%;
        height: 420px;
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        border-radius: 10px;
        overflow: hidden;
    }}
    .news-card:before {{
        content: "";
        position: absolute;
        inset: 0;
        background: linear-gradient(180deg, rgba(0,0,0,0.42) 10%, rgba(0,0,0,0.62) 65%);
        z-index: 0;
    }}
    .overlay-text {{
        position: relative;
        z-index: 2;
        padding: 28px;
        color: white;
        display:flex;
        flex-direction:column;
        align-items:center;
        text-align:center;
        gap:12px;
    }}
    .overlay-text h1 {{
        margin:0;
        font-size:34px;
        font-weight:700;
        line-height:1.05;
        max-width:900px;
    }}

    .meta-row {{
        display:flex;
        gap:12px;
        align-items:center;
        flex-wrap:wrap;
        justify-content:center;
    }}
    .tags span {{
        display:inline-block;
        background:#2563eb;
        color:white;
        padding:6px 12px;
        border-radius:999px;
        font-size:13px;
    }}
    .date {{
        color: #d1d5db;
        font-size:14px;
    }}

    /* Social icons */
    .social-icons {{
        display:flex;
        gap:10px;
        align-items:center;
        margin-top:6px;
    }}
    .social-icons a {{
        display:inline-flex;
        width:44px;
        height:44px;
        border-radius:50%;
        align-items:center;
        justify-content:center;
        color:white;
        text-decoration:none;
        box-shadow: 0 2px 6px rgba(0,0,0,0.18);
        transition: transform .12s ease;
    }}
    .social-icons a:hover {{ transform: translateY(-3px); }}
    .social-icons .fb {{ background:#1877F2; }}
    .social-icons .x  {{ background:#1DA1F2; }}
    .social-icons .li {{ background:#0A66C2; }}
    .social-icons .rd {{ background:#FF4500; }}

    .caption {{
        font-size:13px;
        color: #6b7280;
        margin-top:10px;
    }}
    .summary {{
        background:white;
        color:#111827;
        padding:22px;
        border-radius:10px;
        margin-top:18px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}

    /* Responsive tweaks */
    @media (max-width: 700px) {{
        .news-card {{ height: 360px; }}
        .overlay-text h1 {{ font-size:20px; }}
        .logo-text .logo-main {{ font-size:18px; }}
        .header-buttons {{
            width:100%;
            justify-content:flex-end;
            margin-top:8px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# HTML Content
st.markdown(
    """
    <div class="topbar">
        <div class="logo">
            <i class="fas fa-brain logo-icon" aria-hidden="true"></i>
            <div class="logo-text">
                <span class="logo-main">Neuroscience</span>
                <span class="logo-sub">News.com</span>
            </div>
        </div>
        <div class="header-buttons">
            <a href="#" class="btn-signin">Sign In</a>
            <a href="#" class="btn-help">Help</a>
        </div>
    </div>

    <div class="news-card">
        <div class="overlay-text">
            <h1>Opioid Use in Pregnancy Not Linked to Autism or ADHD Risk</h1>
            <div class="meta-row">
                <div class="tags">
                    <span>Autism</span>
                    <span>Featured</span>
                    <span>Neuroscience</span>
                </div>
                <div class="date">September 16, 2025</div>
            </div>
            <div class="social-icons">
                <a class="fb" href="https://facebook.com" target="_blank"><i class="fab fa-facebook-f"></i></a>
                <a class="x" href="https://twitter.com" target="_blank"><i class="fab fa-x-twitter"></i></a>
                <a class="li" href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                <a class="rd" href="https://reddit.com" target="_blank"><i class="fab fa-reddit-alien"></i></a>
            </div>
        </div>
    </div>

    <div class="caption">
        Similarly, the risk for these neurodevelopmental conditions disappeared when comparing differentially exposed siblings. Credit: Neuroscience News.
    </div>

    <div class="summary">
        <b>Summary:</b> A large-scale study analyzing over a million births in Sweden found no evidence that prescribed opioid pain medications during pregnancy cause autism or ADHD in children. While earlier data raised concerns, this study provides strong evidence to the contrary.
    </div>
    """,
    unsafe_allow_html=True,
)
