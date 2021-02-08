import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)
CWD = os.getcwd()
UPLOAD_FOLDER = os.path.join(CWD, 'uploads')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_PATH'] = 3000000

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/upload')
def render_file_form():
   return render_template('file_submit.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
      return 'file uploaded successfully'

if __name__ == '__main__':
   app.run(debug = True)