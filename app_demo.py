import os, pprint, filetype
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'C:/Users/Laetipoo/Documents'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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
        fileCommonMetadata ={}

        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            fileName = secure_filename(file.filename)
            fileSize = file.filesize
            fileType = filetype.guess(file)
            
            if fileType is None:
            #print('Cannot guess file type!')
                return redirect(request.url)
            elif fileType = 'txt':



                 return jsonify(fileMetadata)
         
            
            fileContent = file.read()
          
            
            fileMetadata = 
            #return redirect(url_for('upload_file',
            #                        filename=filename))
            return pprint.pformat(request.files['file'].read())
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
   app.run(debug=True, port=80, host="0.0.0.0")