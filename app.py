from flask import Flask, request, redirect, url_for, flash, render_template
from werkzeug.utils import secure_filename
import os
from process import op,format_response
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv('secret_key')


@app.route('/')
def index():
    response = request.args.get('response')
    return render_template('index.html', response=response)

@app.route('/submit', methods=['POST'])
def submit():
    if 'pdf' not in request.files:
        flash('No file part')
        return redirect(request.url)
    pdf_file = request.files['pdf']
    if pdf_file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if pdf_file and pdf_file.filename.endswith('.pdf'):
        pdf_filename = secure_filename(pdf_file.filename)
        text_input = request.form['text']
        response = op(pdf=pdf_file, text=text_input)
        formatted_response = format_response(response)
        flash('File successfully uploaded and processed')
        return redirect(url_for('index', response=formatted_response))
    else:
        flash('Invalid file type')
        return redirect(request.url)

if __name__ == "__main__":
    app.run(debug=True)