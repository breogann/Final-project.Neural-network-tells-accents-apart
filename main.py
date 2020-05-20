import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from src.audioClassification import runModel, generateDataframe


#6 CREATING AN API

UPLOAD_FOLDER = 'input'
ALLOWED_EXTENSIONS = {'m4a'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

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
<!DOCTYPE html>
<html lang=“en”>
<center>
<head>
    <meta charset=“UTF-8">
    <meta name=“viewport” content=“width=device-width, initial-scale=1.0">
    <title>Neural network tells accents apart</title>
</head>
<body style="background-color:#946B9C;">
<h1>Which is my accent? 🎙</h1>
<h2>Record yourself reading the following text and upload it so the cat can judge you:</h2>
<p style="text-align:left;"> 🛠 If you're using macOS, open the Voice memo app and drag your voice note to your desktop. Whatsapp voice notes should also work.</p>
<p>"Please call Stella.  Ask her to bring these things with her from the store:  Six spoons of fresh snow peas, five thick slabs of blue cheese, and maybe a snack for her brother Bob.  We also need a small plastic snake and a big toy frog for the kids.  She can scoop these things into three red bags, and we will go meet her Wednesday at the train station."</p>
<form method=post enctype=multipart/form-data>
      <input type=file name=file style="height:40px; width:80px">
      <input type=submit value=⬆️UPLOAD style="height:40px; width:80px">
    </form>
<img src="https://media1.tenor.com/images/0291ad4acb10e5d76bf617e255d130b4/tenor.gif?itemid=12986754"/>
</body>
<center>
</html>
'''

@app.route('/<audioname>', methods=['GET'])
def accent (audioname):
    path = f"input/{audioname}"
    gendf = generateDataframe(path)
    result = runModel(gendf) #To predict  
    return '''
<!DOCTYPE html>
<html lang=“en”>
<center>
<head>
    <meta charset=“UTF-8">
    <meta name=“viewport” content=“width=device-width, initial-scale=1.0">
    <title>Neural network tells accents apart</title>
</head>
<body style="background-color:#946B9C;">
<h1>Which is my accent? 🎙</h1>
<img src="https://media1.tenor.com/images/0291ad4acb10e5d76bf617e255d130b4/tenor.gif?itemid=12986754"/>
<h2>{result}</h2>
<form>
    <input type="button" value="Go back" onclick="history.back()">
</form> 
</body>
<center>
</html>
'''.format(result=result)

app.run('0.0.0.0', port=8080, debug=True, threaded=False) #http://0.0.0.0:3000/