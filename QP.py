# Install packages
!pip -q install google-genai pypdf reportlab

from google import genai
from google.colab import files
from pypdf import PdfReader
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import time

# =========================
# GEMINI API KEY
# =========================
API_KEY = "API_KEY"

client = genai.Client(api_key=API_KEY)

# =========================
# UPLOAD PDF
# =========================
print("Upload Syllabus PDF")
uploaded = files.upload()

pdf_file = list(uploaded.keys())[0]

# =========================
# EXTRACT TEXT
# =========================
reader = PdfReader(pdf_file)

syllabus = ""

for page in reader.pages:
    text = page.extract_text()
    if text:
        syllabus += text + "\n"

print("Syllabus Extracted Successfully!")

# Reduce size if syllabus is huge
if len(syllabus) > 15000:
    syllabus = syllabus[:15000]

# =========================
# PROMPT
# =========================
prompt = f"""
You are an expert university question paper setter.

Generate a question paper STRICTLY from the syllabus below.

SYLLABUS:
{syllabus}

Use EXACTLY this format:

Sri Eshwar College of Engineering

Autonomous Semester End Examination

Degree & Branch:

Subject Code:

Subject Name:

Regulation:

Duration: 3 Hours                    Maximum Marks: 100

Answer ALL Questions

------------------------------------------------------------

PART A – (10 × 2 = 20 Marks)

Generate 10 two-mark questions.

------------------------------------------------------------

PART B – (5 × 16 = 80 Marks)

11. a)

(i) Question

(ii) Question
                                           
                     (OR)

b) Question

12. a)

(i) Question

(ii) Question

                     (OR)

b)

(i) Question

(ii) Question

13. a)

(i) Question

(ii) Question

                     (OR)

b) Question

14. a) Question

                     (OR)

b)

(i) Question

(ii) Question

15. a) Question

                     (OR)

b) Question

------------------------------------------------------------

Rules:

1. Use ONLY topics from syllabus.
2. Cover all units evenly.
3. Avoid duplicate questions.
4. University-level questions.
5. Return only the final question paper.
"""

# =========================
# GENERATE PAPER
# =========================
question_paper = ""

for attempt in range(5):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        question_paper = response.text
        break

    except Exception as e:
        print(f"Attempt {attempt+1} failed")
        print(e)

        if attempt < 4:
            print("Retrying in 15 seconds...")
            time.sleep(15)

if not question_paper:
    raise Exception("Failed to generate question paper.")

print("\nQuestion Paper Generated Successfully!\n")

# =========================
# CREATE PDF
# =========================
pdf_name = "Sri_Eshwar_Question_Paper.pdf"

doc = SimpleDocTemplate(pdf_name)

styles = getSampleStyleSheet()

elements = []

for line in question_paper.split("\n"):
    elements.append(Paragraph(line, styles["Normal"]))
    elements.append(Spacer(1, 3))

doc.build(elements)

print("PDF Created Successfully!")

# =========================
# DOWNLOAD PDF
# =========================
files.download(pdf_name)
