import numpy as np
import pandas as pd
import tensorflow as tf
from keras.utils import load_img
from keras.models import load_model
from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename


tbModel = load_model("Lungs Xray Classification\\98p_model_lungs\\")

def analyzeTB(imagePath):
    img = load_img(imagePath, target_size=(300, 300, 1))
    
    arrImg = tf.image.rgb_to_grayscale(img)
    arrImg = np.array(arrImg) * (1/np.array(arrImg).max())
    arrImg = np.expand_dims(arrImg, axis=0)
 
    pred = tbModel.predict(arrImg) > 0.5
    if pred == True:
        return("Tuberculosis Detected ⚠️")
    else:
        return("XRay is Normal ✅")


app = Flask(__name__)

@app.route("/", methods=["GET"])
def Home():
    try:
        return render_template("home.html")
    except Exception as ex:
        raise ex
    
@app.route("/lungs", methods=["GET"])
def Lungs():
    try:
        return render_template("lungs.html")
    except Exception as ex:
        raise ex

@app.route("/analyzeTB", methods=["GET", "POST"])
def AnalyzeTB():
    try:
        if request.method == "POST":
            fileRequested = request.files["lung-img"]
            print(fileRequested)
            homePath = os.path.dirname(__file__)
            filePath = os.path.join(
                homePath, "uploads", secure_filename(fileRequested.filename)
            )
            fileRequested.save(filePath)
            preds = analyzeTB(filePath)
            result=preds
            return result
        return None
    except Exception as ex:
        raise ex

@app.route("/heart", methods=["GET"])
def Heart():
    try:
        return render_template("heart.html")
    except Exception as ex:
        raise ex

@app.route("/kidney", methods=["GET"])
def Kidney():
    try:
        return render_template("kidney.html")
    except Exception as ex:
        raise ex

if __name__ == "__main__":
    app.run(debug=True)