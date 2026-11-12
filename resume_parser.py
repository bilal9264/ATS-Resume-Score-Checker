
from io import BytesIO
import pymupdf
from docx import Document


def extract_text(uploaded_file):
    file_name = uploaded_file.name.lower()
    file_bytes = uploaded_file.getvalue()

    if file_name.endswith(".pdf"):
        pdf = pymupdf.open(
            stream=file_bytes,
            filetype="pdf"
        )

        text = ""

        for page in pdf:
            text += page.get_text()

        pdf.close()
        return text

    elif file_name.endswith(".docx"):
        document = Document(BytesIO(file_bytes))

        text = ""

        for paragraph in document.paragraphs:
            text += paragraph.text + "\n"

        return text

    else:
        raise ValueError("Unsupported file format")
