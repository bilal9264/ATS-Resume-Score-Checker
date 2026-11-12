
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def analyze_resume(resume_text, job_description):

    prompt = f"""
    You are an expert ATS resume analyzer.

    Analyze the following resume against the job description.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}

    Provide the following analysis:

    1. Estimated ATS Match Score (0-100)
    2. Matching Skills
    3. Missing Skills and Keywords
    4. Weak Areas in the Resume
    5. Suggestions for Improvement

    Be honest and do not invent qualifications
    or experience that the candidate does not have.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
