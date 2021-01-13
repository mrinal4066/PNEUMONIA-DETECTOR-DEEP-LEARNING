# -*- coding: utf-8 -*-

from flask import Flask, render_template,request
import pandas as pd
import numpy as np
import pickle
app = Flask(__name__)

model_name= open("ModelMl.pkl","rb")
model=pickle.load(model_name)


@app.route('/')
def Home():
    return render_template('first.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    
    if request.method == "POST" :
    
        Gender= str(request.form['gender'])
        Ssc_p= float(request.form['ssc_p'])
        Ssc_b = str(request.form['ssc_b'])
        Hsc_p= float(request.form['hsc_p'])
        Hsc_b = str(request.form['hsc_b'])
        Degree_p= float(request.form['degree_p'])
        Degree_t = str(request.form['degree_t'])
        
        if Gender=='Female':
            F=1
        else: 
            F=0
            
        if Ssc_b=='Central':
            Central=1
        else:
            Central=0
        
        if Hsc_b=='Central':
            HsCentral=1
        else:
            HsCentral=0
            
        Comm = 0
        Others = 0
        
        if Degree_t == 'Comm&Mgmt':
            Comm=1
        elif Degree_t=='Others':
            Others=1
           
           
        Pred_args=[Ssc_p,Hsc_p,Degree_p,F,Central,HsCentral,Comm,Others]
        pred_args=np.array(Pred_args)
        pred_args=pred_args.reshape(1,-1)
        
        y_pred=model.predict(pred_args)
        y_pred=y_pred[0]
        if y_pred == 0:
            return render_template('predict.html',prediction="Work Hard!!! Chances are less") 
        else:
            return render_template('predict.html',prediction=" You are Doing well!! You Will Get placements") 
            
            
         
    
if __name__ == '__main__':
    app.run()