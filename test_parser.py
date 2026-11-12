
from resume_parser import extract_text


class TestFile:
    name = "sample_resume.pdf"

    def getvalue(self):
        with open(self.name, "rb") as file:
            return file.read()


resume = TestFile()

text = extract_text(resume)

print("RESUME TEXT:")
print(text)
