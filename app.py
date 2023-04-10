
from flask import Flask,render_template,request,redirect,flash
from werkzeug.utils import secure_filename
import os
import random

UPLOAD_FOLDER ="static/files"
FILE_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#check file extension
def allowed_extensions(file_name):
    return '.' in file_name and file_name.rsplit('.',1)[1].lower() in FILE_EXTENSIONS
           
#file Upload
@app.route("/fileupload",methods=['GET','POST'])
def fileUpload():
    if request.method=='POST':
        if 'file' not in request.files:
            flash('No file part','danger')
            
        file = request.files['file']
        
        if file.filename == '':
            flash('No file selected','danger')
            
        if file and allowed_extensions(file.filename):
            filename, file_extension = os.path.splitext(file.filename)
            new_filename = secure_filename(filename+str(random.randint(10000,99999))+"."+file_extension)
            file.save(os.path.join(UPLOAD_FOLDER, new_filename))   
            
            flash(file.filename+' Uploaded Successfully','success')
            
    return render_template('fileupload.html')
    
if __name__=='__main__':
    app.secret_key='secret123'
    app.run(debug=True)