import streamlit as st
from utils import get_resume_text
from analyzer import analyze_resume

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")

# CSS
st.markdown("""
<style>
/* your CSS here */
</style>
""", unsafe_allow_html=True)

# Title
st.title("🚀 AI Resume Analyzer")
st.write("Get insights, improve your resume, and grow faster.")

# ✅ DEFINE THIS FIRST
uploaded_file = st.file_uploader("Upload Resume (PDF)")

# ✅ THEN USE IT
if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = get_resume_text("temp.pdf")
    result = analyze_resume(text)

    st.info("Analysis Complete ✅")

    # SCORE
    score = result["score"]

    st.markdown(f"""
    <div style="
        background: linear-gradient(145deg, #1a1d24, #0f1116);
        padding: 25px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 6px 30px rgba(0,0,0,0.6);
    ">
        <h2 style="color:#FFD700;">Resume Score</h2>
        <h1 style="font-size:48px; margin:0;">{score}/100</h1>
    </div>
    """, unsafe_allow_html=True)

    st.progress(score / 100)

    # Cards
    def card(title, items):
        st.markdown(f"<div class='card'><h3>{title}</h3>", unsafe_allow_html=True)
        for item in items:
            st.markdown(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)

    card("📌 Key Skills", result["skills"])
    card("💪 Strengths", result["strengths"])
    card("⚠️ Missing Skills", result["missing"])
    card("🎯 Suitable Roles", result["roles"])
    card("🚀 Suggestions", result["suggestions"])