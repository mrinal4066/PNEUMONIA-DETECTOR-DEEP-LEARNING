# -*- coding: utf-8 -*-
#Import necessary libraries
from flask import Flask, render_template, request
 
import numpy as np
import os

from PIL import Image
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
 
#load model
model = load_model('accuracy_88.h5')

 
 
app = Flask(__name__) 


@app.route('/', methods=['GET','POST'])
def Home():
    return render_template('base.html')
    

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method=='POST':

           file=request.files['image']
           filename=file.filename
           print("@@@",filename)
           file_path = os.path.join('static', filename)
           file.save(file_path)
           
           img_width, img_height = 224, 224
           img = image.load_img(file_path, target_size = (img_width, img_height))
           img = image.img_to_array(img)
           img = np.expand_dims(img, axis = 0)
        
           
           ypred=model.predict(img)
        
           print("prediction:",ypred)
        
           if ypred==1:
              rs="PNEUMONIA"
           else:
              rs="NORMAL"
           os.remove(file_path)
           return render_template('base.html',prediction=rs,fp=file_path)
       



if __name__ == '__main__':
    app.run()