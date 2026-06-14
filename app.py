import streamlit as st
import pdfplumber
from groq import Groq

from skills import skills_list
from prompts import generate_prompt

# -----------------------------
# GROQ API
# -----------------------------

client = Groq(
        api_key="PASTE_YOUR_GROQ_API_KEY_HERE"git add .

)

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Interview Readiness Analyzer",
    page_icon="🚀",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------

st.markdown("""
# 🚀 AI Interview Readiness & Skill Gap Analyzer

Compare resumes against job descriptions, identify skill gaps,
calculate interview readiness, generate AI-powered interview questions,
and receive personalized learning recommendations.
""")

# -----------------------------
# INPUTS
# -----------------------------

uploaded_file = st.file_uploader(
    "📄 Upload Resume",
    type=["pdf"]
)

job_description = st.text_area(
    "💼 Paste Job Description"
)

resume_text = ""

# -----------------------------
# MAIN LOGIC
# -----------------------------

if uploaded_file and job_description:

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                resume_text += text

    st.success("✅ Resume Uploaded Successfully")

    resume_text_lower = resume_text.lower()
    jd_text_lower = job_description.lower()

    # -----------------------------
    # SKILL EXTRACTION
    # -----------------------------

    resume_skills = []
    jd_skills = []

    for skill in skills_list:

        if skill.lower() in resume_text_lower:
            resume_skills.append(skill)

        if skill.lower() in jd_text_lower:
            jd_skills.append(skill)

    missing_skills = list(
        set(jd_skills) - set(resume_skills)
    )

    matched_skills = len(jd_skills) - len(missing_skills)

    score = int(
        (matched_skills / max(len(jd_skills), 1))
        * 100
    )

    # -----------------------------
    # READINESS SCORE
    # -----------------------------

    st.subheader("🎯 Interview Readiness Score")

    st.progress(score / 100)

    st.metric(
        label="Readiness Score",
        value=f"{score}%"
    )

    # -----------------------------
    # SKILLS SECTION
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("✅ Skills Found In Resume")

        if resume_skills:
            for skill in resume_skills:
                st.success(skill)
        else:
            st.info("No skills detected.")

    with col2:

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.warning(skill)

        else:

            st.success(
                "Great! No missing skills detected."
            )

    # -----------------------------
    # LEARNING ROADMAP
    # -----------------------------

    st.subheader(
        "📚 Personalized Learning Roadmap"
    )

    if missing_skills:

        for week, skill in enumerate(
            missing_skills[:10],
            start=1
        ):

            st.info(
                f"Week {week}: Learn {skill}"
            )

    else:

        st.success(
            "You are already aligned with the job requirements."
        )

    # -----------------------------
    # IMPROVEMENT SUGGESTIONS
    # -----------------------------

    st.subheader(
        "💡 Improvement Suggestions"
    )

    if missing_skills:

        for skill in missing_skills[:5]:

            st.write(
                f"• Improve proficiency in **{skill}**"
            )

    else:

        st.write(
            "• Continue practicing interview questions."
        )

    # -----------------------------
    # AI QUESTIONS
    # -----------------------------

    prompt = generate_prompt(
        resume_text,
        job_description
    )

    try:

        with st.spinner(
            "Generating AI Interview Questions..."
        ):

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

        st.subheader(
            "🤖 AI Interview Questions & Suggestions"
        )

        st.write(
            response.choices[0].message.content
        )

    except Exception as e:

        st.error(
            f"AI Generation Error: {e}"
        )
