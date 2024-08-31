from dotenv import load_dotenv
import google.generativeai as genai
import os
import PyPDF2 as pdf

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Gemini Response

def get_gemini_response(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    
    return response.text 

# Extract text from pdf
def pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    
    for page in range(len(reader.pages)):
        page=reader.pages[page]
        text += str(page.extract_text())
        
    return text        

# Prompt Template
prompt="""
        Act as a Skilled and very experiended ATS(Application Tracking System) with a deep understading of IT field, software engineering, data science, data analysis, big data engineering, Generative ai etc. Your task is to evaluate the resume based on given job description. Consider that job market is very compititive and you should provide best assistance for improving the resumes. Assign percentage matching based on job description and the missing keywords with high accuracy.
        This is resume : {text} 
        This is job description: {jd}
        
        give me response in this format{{"Matching Percent": "%","Missing Keywords": [],
        "Profile Summary":" "
        }}
"""

