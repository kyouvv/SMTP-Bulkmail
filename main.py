from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os
from smtp import extractRecipients, sendEmail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'smtlpclient'
app.config['UPLOAD_FOLDER'] = 'static/uploads'  # Define the directory to store uploaded files

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        email = request.form['emailInput']
        password = request.form['passInput']
        subject = request.form['subjectInput']
        content = request.form['contentInput']
        data = request.files['csvUpload']
        header = request.form['headerText']
        footer = request.form['footerText']

        if data and header and footer:
            # Save uploaded files
            if not os.path.exists('static/uploads'):
                os.makedirs('static/uploads')
            data_filename = secure_filename(data.filename)

            data.save(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))

        recipients = extractRecipients(os.path.join(app.config['UPLOAD_FOLDER'], data_filename))
        sendEmail(email, password, subject, content, header, footer, recipients)
        
        return render_template('home.html')
        
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)