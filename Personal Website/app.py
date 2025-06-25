import streamlit as st
from PIL import Image
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nikulkumar Dabhi | Data Scientist & AI Enthusiast", page_icon="🤖", layout="wide")

# --- HELPER FOR BACKGROUND IMAGE ---
def set_bg_image(image_path):
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
        encoded = base64.b64encode(img_bytes).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/jpg;base64,{encoded}');
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
    """, unsafe_allow_html=True)

# --- CUSTOM CSS FOR MODERN LOOK ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Montserrat', sans-serif;
        background: #FFC72C !important;
    }
    .main > div {
        background: transparent !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        margin-bottom: 0;
        padding: 0;
    }
    .section-title {
        color: #DA291C;
        font-size: 2.2rem;
        font-weight: 700;
        margin-top: 2.5rem;
        margin-bottom: 1.2rem;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .section-divider {
        border: none;
        border-top: 2.5px solid #FFC72C;
        margin: 2.5rem 0 2.5rem 0;
    }
    .highlight {
        background: #FFF3C0;
        border-radius: 0.5rem;
        padding: 0.6rem 1.2rem;
        margin-bottom: 1rem;
        display: inline-block;
        color: #DA291C;
        font-size: 1.05rem;
        transition: box-shadow 0.3s;
        border-left: 6px solid #DA291C;
    }
    .highlight:hover {
        box-shadow: 0 4px 16px 0 rgba(218,41,28,0.13);
    }
    .sidebar-section {
        background: #FFF3C0;
        border-radius: 1.2rem;
        padding: 2rem 1.2rem 1.2rem 1.2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 12px 0 rgba(218,41,28,0.08);
        position: sticky;
        top: 2rem;
        max-height: 260px;
        overflow: auto;
    }
    .sidebar-link {
        color: #DA291C !important;
        font-weight: 500;
        text-decoration: none !important;
        margin-bottom: 0.2rem;
        display: flex;
        align-items: center;
        gap: 0.4rem;
    }
    .sidebar-link:hover {
        text-decoration: underline !important;
        color: #FFC72C !important;
        background: #DA291C11;
    }
    .quick-links {
        margin-top: 1.5rem;
    }
    .main-content {
        background: transparent !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        margin-bottom: 0;
        padding: 0 0 2rem 0;
    }
    .project-card {
        background: #FFF3C0;
        border-radius: 1rem;
        box-shadow: 0 2px 8px 0 rgba(218,41,28,0.08);
        padding: 1.2rem 1rem 1rem 1rem;
        margin-bottom: 1.2rem;
        transition: transform 0.2s, box-shadow 0.2s;
        min-height: 320px;
    }
    .project-card:hover {
        transform: translateY(-6px) scale(1.03);
        box-shadow: 0 8px 24px 0 rgba(218,41,28,0.18);\
    }
    .project-img {
        width: 100%;
        border-radius: 0.7rem;
        margin-bottom: 0.7rem;
        object-fit: cover;
        height: 120px;
        border: 2px solid #FFC72C;
    }
    .badge {
        display: inline-block;
        background: #FFC72C;
        color: #DA291C;
        border-radius: 0.5rem;
        padding: 0.2rem 0.7rem;
        font-size: 0.9rem;
        margin-right: 0.4rem;
        margin-bottom: 0.3rem;
        font-weight: 600;
    }
    .timeline {
        border-left: 3px solid #FFC72C;
        margin-left: 1.2rem;
        padding-left: 1.2rem;
    }
    .timeline-event {
        margin-bottom: 1.5rem;
        position: relative;
    }
    .timeline-event:before {
        content: '';
        position: absolute;
        left: -1.35rem;
        top: 0.3rem;
        width: 0.9rem;
        height: 0.9rem;
        background: #FFC72C;
        border-radius: 50%;
        border: 2px solid #fff;
        box-shadow: 0 0 0 2px #DA291C22;
    }
    .progress-bar {
        background: #FFE082;
        border-radius: 0.5rem;
        height: 18px;
        margin-bottom: 0.7rem;
        width: 100%;
        position: relative;
    }
    .progress {
        background: linear-gradient(90deg, #FFC72C 60%, #DA291C 100%);
        height: 100%;
        border-radius: 0.5rem;
        transition: width 0.7s;
    }
    .contact-icon {
        font-size: 1.3rem;
        margin-right: 0.7rem;
        color: #DA291C;
    }
    .sidebar-section .tab-link {
        display: block;
        background: #FFC72C;
        color: #DA291C !important;
        font-weight: 700;
        border-radius: 0.7rem;
        padding: 0.7rem 1.2rem;
        margin-bottom: 0.7rem;
        text-align: center;
        text-decoration: none !important;
        box-shadow: 0 2px 8px 0 rgba(218,41,28,0.08);
        transition: background 0.2s, color 0.2s, box-shadow 0.2s;
        border: 2px solid #FFC72C;
    }
    .sidebar-section .tab-link:hover, .sidebar-section .tab-link:active {
        background: #DA291C;
        color: #fff !important;
        border: 2px solid #DA291C;
        box-shadow: 0 4px 16px 0 rgba(218,41,28,0.13);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- OPTIONAL: SET BACKGROUND IMAGE (comment out if not wanted) ---
# set_bg_image("Personal Website/profile.jpg")

# --- SIDEBAR ---
with st.sidebar:
    st.image("Personal Website/profile.jpg", width=225)
    st.markdown('<div class="sidebar-section" style="background:transparent;box-shadow:none;padding-top:0;">', unsafe_allow_html=True)
    st.markdown(
        """
        <div class='quick-links' style='margin-top:0;display:flex;flex-direction:column;gap:1rem;align-items:center;'>
            <a class='sidebar-tab-link' href='#projects'>🚀 Projects</a>
            <a class='sidebar-tab-link' href='#experience'>💼 Experience</a>
            <a class='sidebar-tab-link' href='#skills'>🛠️ Skills</a>
            <a class='sidebar-tab-link' href='#education'>🎓 Education</a>
            <a class='sidebar-tab-link' href='#contact'>📬 Contact</a>
        </div>
        <style>
        .sidebar-section {
            background: transparent !important;
            box-shadow: none !important;
            padding-top: 0 !important;
            max-height: 420px !important;
            padding-bottom: 2.5rem !important;
        }
        .sidebar-tab-link {
            display: block;
            background: #FFC72C;
            color: #DA291C !important;
            font-weight: 800;
            font-size: 1.15rem;
            border-radius: 1.2rem;
            padding: 1.1rem 1.5rem;
            text-align: center;
            text-decoration: none !important;
            box-shadow: 0 4px 16px 0 rgba(218,41,28,0.13);
            transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.1s;
            border: 2.5px solid #FFC72C;
            letter-spacing: 0.5px;
            margin: 0;
            width: 210px;
            max-width: 100%;
        }
        .sidebar-tab-link:hover, .sidebar-tab-link:active {
            background: #DA291C;
            color: #fff !important;
            border: 2.5px solid #DA291C;
            box-shadow: 0 8px 24px 0 rgba(218,41,28,0.18);
            transform: scale(1.04);
        }
        @media (max-width: 350px) {
            .sidebar-tab-link {
                width: 100% !important;
                font-size: 1rem;
                padding: 0.8rem 0.5rem;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown('</div>', unsafe_allow_html=True)

# Update tab-link style for larger, more prominent tabs and transparent sidebar
st.markdown(
    """
    <style>
    .sidebar-section {
        background: transparent !important;
        box-shadow: none !important;
        padding-top: 0 !important;
    }
    .sidebar-section .tab-link {
        display: block;
        background: #FFC72C;
        color: #DA291C !important;
        font-weight: 800;
        font-size: 1.25rem;
        border-radius: 1.2rem;
        padding: 1.1rem 1.5rem;
        margin-bottom: 1.1rem;
        text-align: center;
        text-decoration: none !important;
        box-shadow: 0 4px 16px 0 rgba(218,41,28,0.13);
        transition: background 0.2s, color 0.2s, box-shadow 0.2s, transform 0.1s;
        border: 2.5px solid #FFC72C;
        letter-spacing: 0.5px;
    }
    .sidebar-section .tab-link:hover, .sidebar-section .tab-link:active {
        background: #DA291C;
        color: #fff !important;
        border: 2.5px solid #DA291C;
        box-shadow: 0 8px 24px 0 rgba(218,41,28,0.18);
        transform: scale(1.04);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- MAIN CONTENT ---
st.markdown('<div class="main-content">', unsafe_allow_html=True)

# --- HEADER SECTION (PROFILE + NAME/TAGLINE) ---
# Get absolute paths for images
image_dir = os.path.dirname(__file__)
profile_path = os.path.join(image_dir, "profile.jpg")

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

profile_base64 = get_base64_image(profile_path)

# Remove gap above header
st.markdown('<style>.main-content { margin-top: 0 !important; padding-top: 0 !important; }</style>', unsafe_allow_html=True)
st.markdown('<style>div.block-container { padding-top: 0rem !important; margin-top: 0 !important; }</style>', unsafe_allow_html=True)

# Extra clearance at the top
st.markdown(f"""
    <div style=\"margin-top:2.5rem;\"></div>
    <div style=\"display:flex;flex-direction:row;align-items:center;justify-content:center;margin-top:0.5rem;margin-bottom:2.2rem;gap:2.2rem;\">
        <img src=\"data:image/jpeg;base64,{profile_base64}\" style=\"width:160px;height:160px;border-radius:18px;object-fit:cover;box-shadow:0 2px 12px 0 rgba(60,60,60,0.10);margin:0;\" alt=\"Profile\">
        <div style=\"text-align:left;\">
            <div style=\"font-size:2.5rem;font-weight:800;letter-spacing:1px;color:#fff;\">Nikulkumar Dabhi</div>
            <div style=\"font-size:1.25rem;color:#3949ab;font-weight:600;margin-top:0.2rem;\">Data Scientist & AI Enthusiast</div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- REDUCE GAP ABOVE BANNER ---
st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- HIGHLIGHTS OF QUALIFICATIONS ---
st.markdown('<div class="section-title">🌟 Highlights of Qualifications</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div style='margin-bottom:1.2rem;'>
        <div class='highlight'>McMaster University graduate with 1 year of co-op experience in data modeling and analysis of real-world projects.</div><br>
        <div class='highlight'>Proficient in Python, SQL, NumPy, Pandas, Matplotlib, Plotly, Seaborn, Scikit-learn, Power BI, Tableau, ArcGIS Pro.</div><br>
        <div class='highlight'>Team player with analytical thinking and strong communication skills to support data-driven decision-making and deliver innovative solutions.</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- EDUCATION (TIMELINE) ---
st.markdown('<div class="section-title" id="education">🎓 Education</div>', unsafe_allow_html=True)
st.markdown('<div class="timeline">', unsafe_allow_html=True)
st.markdown(
    """
    <div class='timeline-event'>
        <b>Master of Engineering (Co-op), Manufacturing Engineering</b><br>
        McMaster University, Hamilton, ON, Canada<br>
        <span style='color:#3949ab;'>Jan 2023 - Dec 2024</span><br>
        Transcript W Grade: A+
    </div>
    <div class='timeline-event'>
        <b>Bachelor of Engineering, Mechanical Engineering</b><br>
        Gujarat Technological University, Gujarat, India<br>
        <span style='color:#3949ab;'>Jul 2017 - Jun 2021</span><br>
        Transcript W Grade: A+
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- EXPERIENCE (TIMELINE) ---
st.markdown('<div class="section-title" id="experience">💼 Experience</div>', unsafe_allow_html=True)
st.markdown('<div class="timeline">', unsafe_allow_html=True)
st.markdown(
    """
    <div class='timeline-event'>
        <b>Research Assistant Co-Op | McMaster University, Hamilton, ON (On-site)</b><br>
        <span style='color:#3949ab;'>Jan 2024 - Aug 2024</span><br>
        <ul>
        <li>Conducted Techno-Economic Analysis to evaluate the feasibility of sustainable BMED plant deployment, assessing factors such as energy, land, labor costs, and carbon markets. Co-authored and published findings in a research paper.</li>
        <li>Applied advanced analytics and geospatial data visualization techniques in ArcGIS Pro to transform complex datasets into strategic insights, contributing to a recommendation framework for cost-efficient and sustainable plant site selection.</li>
        <li>Engineered ETL data pipelines using Python to streamline geospatial data processing, expedite report generation, and enhance the accuracy of scenario evaluations, supporting data-driven decision-making.</li>
        </ul>
    </div>
    <div class='timeline-event'>
        <b>Web Developer Network Specialist (Part-time) | McMaster University, ON (On-site)</b><br>
        <span style='color:#3949ab;'>Sep 2023 - Dec 2024</span><br>
        <ul>
        <li>Developed and maintained the department website, implementing A/B testing to optimize the user experience.</li>
        <li>Collaborated with faculty, admin, web developers, and students to gather requirements and deliver web solutions.</li>
        </ul>
    </div>
    <div class='timeline-event'>
        <b>Design and Validation Engineering Co-op | Linamar Corporation, Guelph, ON (On-site)</b><br>
        <span style='color:#3949ab;'>Sep 2023 - Dec 2023</span><br>
        <ul>
        <li>Utilized Power BI to create interactive dashboards and integrated them with MS Project for real-time KPI tracking and project performance monitoring, providing actionable insights that improved decision-making by 25%.</li>
        <li>Automated data retrieval and processing tasks using Excel macros and VBA to reduce manual efforts by 40%, eliminate redundancy, and accelerate data analysis workflows, improving accuracy and reducing execution times.</li>
        </ul>
    </div>
    """,
    unsafe_allow_html=True,
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- SKILLS (BADGES & PROGRESS BARS) ---
st.markdown('<div class="section-title" id="skills">🛠️ Skills</div>', unsafe_allow_html=True)

# Grouped skills by category
skill_groups = {
    "Programming & Data": [
        "Python", "SQL", "MATLAB", "Minitab", "Simul8", "Git", "LaTeX"
    ],
    "Business Intelligence & Analytics": [
        "Power BI", "Tableau", "DAX", "Excel (Macros & VBA)", "MS Project", "MS Office Suite"
    ],
    "AI & Machine Learning": [
        "Machine Learning", "Deep Learning", "Generative AI & LLMs", "Prompt Engineering", "AI Agents"
    ],
    "Geospatial & Visualization": [
        "ArcGIS Pro", "Notion", "WordPress", "HTML", "Google Sites"
    ],
    "Project & Process": [
        "Agile", "Lean Six Sigma (Green Belt)"
    ]
}
soft_skills = [
    "Organization", "Time Management", "Communication", "Problem Solving", "Analytical Thinking", "Teamwork", "Quick Learner"
]

for group, skills in skill_groups.items():
    st.markdown(f"<span style='color:#DA291C;font-size:1.15rem;font-weight:700;margin-bottom:0.2rem;display:inline-block;'>{group}</span>", unsafe_allow_html=True)
    st.markdown(", ".join([f"<span class='badge'>{s}</span>" for s in skills]), unsafe_allow_html=True)

# Soft Skills in the same format
st.markdown(f"<span style='color:#DA291C;font-size:1.15rem;font-weight:700;margin-bottom:0.2rem;display:inline-block;'>Soft Skills</span>", unsafe_allow_html=True)
st.markdown(", ".join([f"<span class='badge'>{s}</span>" for s in soft_skills]), unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- PROJECTS (CARDS) ---
st.markdown('<div class="section-title" id="projects">🚀 Projects</div>', unsafe_allow_html=True)

project_data = [
    {
        "title": "Deep Neural Network",
        "desc": "Developed a deep neural network for image classification with 95%+ accuracy on test data.",
        "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=400&q=80",
        "tags": ["Deep Learning", "Python", "TensorFlow"],
        "github": "https://github.com/Nikulkumar-Dabhi/deep-neural-network"
    },
    {
        "title": "Geospatial Analytics Pipeline",
        "desc": "Built an ETL pipeline for geospatial data, automating data cleaning, transformation, and visualization.",
        "img": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=400&q=80",
        "tags": ["ETL", "Python", "ArcGIS Pro"],
        "github": "https://github.com/Nikulkumar-Dabhi/geospatial-analytics-pipeline"
    },
    {
        "title": "Interactive BI Dashboard",
        "desc": "Designed a Power BI dashboard for real-time KPI tracking, improving decision-making by 25%.",
        "img": "https://images.unsplash.com/photo-1519389950473-47ba0277781c?auto=format&fit=crop&w=400&q=80",
        "tags": ["Power BI", "Dashboard", "KPI"],
        "github": "https://github.com/Nikulkumar-Dabhi/interactive-bi-dashboard"
    }
]

cols = st.columns(3)
for i, proj in enumerate(project_data):
    with cols[i % 3]:
        st.markdown(f"""
            <div class='project-card'>
                <img src='{proj['img']}' class='project-img' alt='Project image'>
                <div style='font-size:1.15rem;font-weight:700;margin-bottom:0.3rem;'>{proj['title']}</div>
                <div style='font-size:0.98rem;color:#444;margin-bottom:0.5rem;'>{proj['desc']}</div>
                <div style='margin-bottom:0.5rem;'>
                    {''.join([f"<span class='badge'>{tag}</span>" for tag in proj['tags']])}
                </div>
                <a href='{proj['github']}' target='_blank' class='sidebar-link'>🔗 View on GitHub</a>
            </div>
        """, unsafe_allow_html=True)

st.markdown('<hr class="section-divider">', unsafe_allow_html=True)

# --- CONTACT SECTION (FORM) ---
st.markdown('<div class="section-title" id="contact">📬 Contact</div>', unsafe_allow_html=True)
# Removed contact form and symbols from contact info
st.markdown("""
- <b>Email:</b> <a href='mailto:dabhinikulsinh9@gmail.com'>dabhinikulsinh9@gmail.com</a><br>
- <b>Mobile:</b> +1 (647) 671-8592<br>
- <b>LinkedIn:</b> <a href='https://www.linkedin.com/in/nikulkumar-dabhi/' target='_blank'>linkedin.com/in/nikulkumar-dabhi</a><br>
- <b>GitHub:</b> <a href='https://github.com/Nikulkumar-Dabhi' target='_blank'>github.com/Nikulkumar-Dabhi</a>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) 