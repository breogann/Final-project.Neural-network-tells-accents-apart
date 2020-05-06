import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from audioClassification import runModel, generateDataframe

#6 CREATING AN API

UPLOAD_FOLDER = '../input'
ALLOWED_EXTENSIONS = {'m4a'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

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
            to = filename
            return redirect(to)
    return '''
     <center>
    <!doctype html>
    <title>Neural network tells accents apart</title>
    <h1>Which is my accent? 🎙</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=⬆️UPLOAD>
    </form>
    </center>
    '''

@app.route('/<audioname>', methods=['GET'])
def accent (audioname):
    path = f"../input/{audioname}"
    gendf = generateDataframe(path)
    result = runModel(gendf) #To predict 
    return result

app.run('0.0.0.0', port=3000, debug=False, threaded=False) #http://0.0.0.0:3000/