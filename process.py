import os
import PyPDF2
#from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
import google.generativeai as genai
from google.generativeai import GenerativeModel
genai.configure(api_key=os.getenv('gemini_key'))

def format_response(response):
    formatted_response = response.replace('**', '').replace('*', '')
    formatted_response = formatted_response.replace('\n', '<br>')
    sections = formatted_response.split("**")
    html_content = ""
    for section in sections:
        if ':' in section:
            title, content = section.split(":", 1)
            html_content += f"<h3>{title.strip()}:</h3><p>{content.strip()}</p>"
        else:
            html_content += f"<p>{section.strip()}</p>"

    return html_content

def extract_text_from_pdf(pdf_file):
    text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page in pdf_reader.pages:
        text += page.extract_text()
    print(text)
    return text

def get_gemini_pro_corrections(resume_text, job_description):
    model = GenerativeModel('gemini-1.5-flash')

    prompt = f"Analyze the following resume and job description, and provide corrections to improve the resume, your main " \
             f"aim is to make the resume more ATS friendly, assume that there is no issues with the readability of the resume" \
             f"provide improvement strictly based on the content of the resume" \
             f"The suggestions should be point wise short and in around 100 words." \
             f":\n\nResume:\n{resume_text}\n\nJob Description:\n{job_description}"

    response = model.generate_content(prompt)
    return response.text

def op(pdf, text):
    pdf_text = extract_text_from_pdf(pdf)
    corrections = get_gemini_pro_corrections(pdf_text, text)
    return corrections
