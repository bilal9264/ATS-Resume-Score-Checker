
import streamlit as st

from resume_parser import extract_text
from ats_analyzer import analyze_resume


# Page configuration
st.set_page_config(
    page_title="ATS Resume Checker",
    page_icon="📄",
    layout="centered"
)

# Application heading
st.title("📄 ATS Resume Score Checker by BILAL AHMAD")

st.write(
    "Upload your resume and paste a job description "
    "to discover how well your resume matches the job."
)

st.divider()

# Resume upload
st.subheader("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume",
    type=["pdf", "docx"]
)

# Job description
st.subheader("2. Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=250,
    placeholder="Paste the complete job description..."
)

# Analyze button
if st.button("Analyze My Resume", type="primary"):

    if uploaded_file is None:
        st.warning("Please upload your resume.")

    elif not job_description.strip():
        st.warning("Please enter a job description.")

    else:
        with st.spinner("Analyzing your resume..."):

            try:
                resume_text = extract_text(uploaded_file)

                if not resume_text.strip():
                    st.error("Could not extract text from this resume.")
                else:
                    result = analyze_resume(
                        resume_text,
                        job_description
                    )

                    st.success("Analysis completed!")

                    st.subheader("Your Resume Analysis")
                    st.markdown(result)

            except Exception as e:
                st.error(f"Something went wrong: {e}")
