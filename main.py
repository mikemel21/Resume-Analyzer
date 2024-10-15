import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GOOGLEAI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")
pdf_input = genai.upload_file("/home/mike/Documents/resume-analyzer/SAMPLEComputer-Science-Resume.pdf")
response = model.generate_content(["Given this resume, analyze the content and review the good and bad parts of it.", pdf_input])


print(response.text)
