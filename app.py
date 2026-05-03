import streamlit as st
from utils import get_resume_text
from analyzer import analyze_resume

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    text = get_resume_text("temp.pdf")

    st.subheader("Analyzing...")
    result = analyze_resume(text)

    st.subheader("Result")
    st.write(result)
    