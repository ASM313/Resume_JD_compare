from flask import Flask, render_template, request
from utils import *

app = Flask(__name__)

@app.route('/')
def index():
    # return "Asslamu alaikum"
    return render_template("index.html")

@app.route('/compare', methods=['GET', 'POST'])
def compare():
    if request.method == 'POST':
        # Take from user
        resume = request.files['resume']
        job_description = request.form['job_description']
        
        # Extract text from the uploaded PDF resume
        resume_text = pdf_text(resume)
        
        # Write prompt
        prompt = prompt_template(resume_text, job_description)

        # Get response from Gemini
        gemini_response =  get_gemini_response(prompt)
        
        print(gemini_response)
        return render_template('index.html', result=gemini_response)
    return render_template('index.html', result=None)
    # return "Successfull"
    

if __name__=="__main__":
    app.run(debug=True)
