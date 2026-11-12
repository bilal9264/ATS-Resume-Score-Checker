
from resume_parser import extract_text
from ats_analyzer import analyze_resume


class TestFile:
    name = "sample_resume.pdf"

    def getvalue(self):
        with open(self.name, "rb") as file:
            return file.read()


# Extract resume text
resume = TestFile()
resume_text = extract_text(resume)

# Sample job description
job_description = """
We are looking for a Junior Python Developer.

Requirements:
- Python programming
- Basic SQL knowledge
- Problem-solving skills
- Knowledge of Git and GitHub
- Understanding of data structures
"""


# Analyse the resume
print("Analysing your resume...")

result = analyze_resume(resume_text, job_description)

print("\nATS ANALYSIS RESULTS:\n")
print(result)
