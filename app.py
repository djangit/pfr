import os, pprint, filetype, base64, json, magic
from flask import Flask, flash, request, redirect, url_for, jsonify
from werkzeug.utils import secure_filename
#from mimetypes import MimeTypes
#from flasgger import Swagger
import connexion


UPLOAD_FOLDER = '/home/lpirbay/Documents/pfr'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv'}

#app = Flask(__name__)
#swagger = Swagger(app)

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

#@app.route('/', methods=['POST'])
def upload_file():
    fileMetadata ={}

        # check if the post request has the file part
    if 'file' not in request.files:
        return ('No file part in the request')
        
    file = request.files['file']
    #request.files.get('file')


        # if user does not select file, browser also
        # submit an empty part without filename
    if file.filename == '':
        return ('No selected file')


    if file and allowed_file(file.filename):
        content=base64.b64encode(file.read())# il faut encoder le contenu qui n'est pas de type texte pour que ca puisse aller dans un fichier json
        fileMetadata['name']=file.filename
        fileMetadata['size']=len(content)
        fileMetadata['mimetype']=file.content_type
        #fileMetadata['mimetype']=magic.Magic(mime=True).from_file(file)
        #fileMetadata['mimetype']=MimeTypes().guess_type(file)

        # le contenu va dependre du type de fichier
        fileType = filetype.guess(file)
        
        if fileType is None:
            #si le type est inconnu on suppose que le fichier est un fichier de type texte (csv,json,xml,txt etc ...)
            try:
                fileMetadata['content']=content.decode()
            except:
                return 'File format not supported'                
        else:
        #Le type de fichier est connu
            fileMetadata['extension']= fileType.extension
          
    else :
        return('File not supported : please upload a csv, png or txt file')
        
    return jsonify(fileMetadata), 200
        


if __name__ == "__main__":
    app = connexion.FlaskApp(__name__, port=9090, specification_dir='')
    app.add_api('api.yml')
    app.secret_key = 'super secret key'
    app.run(debug=True, port=8000, host="0.0.0.0")
   