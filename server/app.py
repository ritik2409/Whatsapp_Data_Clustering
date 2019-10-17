# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 11:32:05 2019

@author: Ritik Gupta
"""

from flask import Flask,request,send_file,render_template,json
from werkzeug import secure_filename
import os
import zipfile
import io
import sys
import gensim
from config import *
sys.path.append(sys_path)

#loadig google pretrained model
print('Model Loading')
model = gensim.models.KeyedVectors.load_word2vec_format(sys_path + '/GoogleNews-vectors-negative300.bin', binary=True)  
print("Loaded model successully")


app = Flask(__name__)

from cleaning import *
from whatsapp_clusters import *


#loading html template
@app.route("/")
def FrontPage():
    return render_template('template.html')

#handleUpload is the form action in html template
@app.route("/handleUpload",methods = ['POST'])
def getfile():
    
    #checking if file is uploaded or not
    if 'file' not in request.files:
        return  app.response_class(
                response=json.dumps({"status":"No File Part"}),
                status=400,
                mimetype='application/json')
        
    #getting cluster_value and required file
    cluster_value = request.form['cluster_value']    
    file = request.files['file']
    
    #checking for successful file
    if file.filename == '':
            return  app.response_class(
                response=json.dumps({"status":"No selected file"}),
                status=400,
                mimetype='application/json')
      
    #getting filename    
    filename = secure_filename(file.filename)
    
    #checking for txt extension in the file
    if not filename.lower().endswith('.txt'):
        return  app.response_class(
                response=json.dumps({"status":"Incorrect File Type"}),
                status=400,
                mimetype='application/json')
    
    #saving file in the required destination    
    file.save(os.path.join(Upload_folder,filename))
    if os.stat(Upload_folder+"/"+filename).st_size == 0:
        return app.response_class(
                response=json.dumps({"status":"Empty Text File"}),
                status=500,
                mimetype='application/json')
        
    app.logger.info('File Successfully Saved',filename)
    
    #cleaning file with clean function in cleaning.py
    clean(Upload_folder+"/"+filename)
    
    #clustering with clusters function in whatsapp_clusters.py
    clusters(int(cluster_value),model)
    app.logger.info('Numpy array created',filename)

    #getting the path of the folder where files were created 
    path = writeFile(Upload_folder)
    
    #creating a zip folder
    datazip = io.BytesIO()
    with zipfile.ZipFile(datazip, 'w', zipfile.ZIP_DEFLATED) as z:
        for root,dirs,files in os.walk(path):
                for filename in files:
                        filepath = os.path.join(root,filename)
                        z.write(filepath, filepath[len(path):])  
    datazip.seek(0)
     
    return send_file(
        datazip,
        as_attachment=True,
        attachment_filename=os.path.basename(path)+'.zip')
    
if __name__ == '__main__':
    app.logger.info('Running sucessfully')
    app.run(host ='0.0.0.0',debug = True)
