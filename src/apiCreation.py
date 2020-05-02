import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import send_from_directory
from audioClassification import generateDataframe, runModel
from os.path import join, dirname, realpath

#6 CREATING AN API

UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'input')
ALLOWED_EXTENSIONS = {'m4a'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/test")
def test ():
    return {"Success":"The API works!"}
    
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            to = "/predict/"+filename
            print(to)
            return redirect(to)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method='post' enctype='multipart/form-data'>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/input/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/predict/<filename>', methods=['GET'])
def recordedAudio (filename):
    path = f"../outputs/{filename}"
    return runModel(generateDataframe(path))

app.run('0.0.0.0', port=5000, debug=False, threaded=False)