import streamlit as st
from PIL import Image

# --- CONFIG ---
st.set_page_config(page_title="Nikulsinh Dabhi | Data Scientist & AI Enthusiast", page_icon="🤖", layout="wide")

# --- HERO SECTION ---
st.markdown("""
    <style>
    .hero {
        text-align: center;
        padding: 3rem 0 2rem 0;
    }
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    .hero-tagline {
        font-size: 1.5rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .hero-btn {
        background: #2563eb;
        color: white;
        padding: 0.75rem 2rem;
        border-radius: 2rem;
        font-size: 1.1rem;
        text-decoration: none;
        transition: background 0.2s;
    }
    .hero-btn:hover {
        background: #1d4ed8;
    }
    </style>
    <div class="hero">
        <div class="hero-title">Nikulsinh Dabhi</div>
        <div class="hero-tagline">Data Scientist & AI Enthusiast</div>
        <a class="hero-btn" href="#contact">Contact Me</a>
    </div>
""", unsafe_allow_html=True)

# --- ABOUT SECTION ---
st.header("About Me")
st.write(
    """
    Hi! I'm Nikulsinh Dabhi, a passionate Data Scientist and AI Enthusiast. I love building intelligent systems, exploring data, and sharing knowledge. 
    My interests include machine learning, deep learning, and deploying AI solutions that make a difference.
    """
)

# --- PROJECTS SECTION ---
st.header("Projects")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Project One")
    st.write("Short description of project one.")
    st.link_button("View on GitHub", "https://github.com/yourusername/project1")
with col2:
    st.subheader("Project Two")
    st.write("Short description of project two.")
    st.link_button("View on GitHub", "https://github.com/yourusername/project2")
with col3:
    st.subheader("Project Three")
    st.write("Short description of project three.")
    st.link_button("View on GitHub", "https://github.com/yourusername/project3")

# --- CONTACT/SOCIALS SECTION ---
st.header("Contact & Socials", anchor="contact")
st.write("Feel free to connect with me!")
st.markdown("""
- [LinkedIn](https://www.linkedin.com/in/yourlinkedin)
- [GitHub](https://github.com/yourusername)
- [Email](mailto:your.email@example.com)
""") 