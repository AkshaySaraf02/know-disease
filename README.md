# KnowDisease - An ML Health Diagnostic 👨🏻‍⚕️
## Table of Content
  * [Overview](#overview)
  * [User Interface](#user-interface)
  * [Demo](#demo)
  * [Goals](#goals)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [To Do](#to-do)
  * [Technologies Used](#technologies-used)
  * [LICENSE](#license)

## Overview
KnowDisease is an web based application that utilizes machine learning technology to diagnose lung tuberculosis by analyzing X-rays as the input. It is built on a convolutional neural network (CNN) model and relies on powerful libraries such as Flask, TensorFlow, Keras, and SciKit Learn for its backend. For the frontend, KnowDisease employs HTML, CSS, and JavaScript. The classification model used by KnowDisease has been trained on a dataset consisting of over 1000 X-ray images.

## User Interface
<p align="left">
  <img src="KnowDisease1.png" width="500">
</p>
<p align="center">
  <img src="KnowDisease2.png" width="500">
</p>

## Demo

Here is the operational demonstration of the application.
<p align="left">
  <img src="KnowDisease Working.gif" width="500">
</p>

## Goals
* Tuberculosis is a deadly disease that affects millions of people worldwide.
* Traditional methods of diagnosis are time-consuming and often unreliable.
* KnowDisease aims to provide an accurate and efficient diagnostic tool using machine learning technology to analyze X-ray images of the lungs for signs of tuberculosis.

## Technical Aspect
The app is built in 3 stages.

1️⃣  The model was trained on a dataset of over 1000 lung X-rays, consisting of both infected and normal cases, using the deep learning technique, convolutional neural networks (CNN).

2️⃣  The front end or user interface was developed using HTML and CSS, with a touch of JavaScript.

3️⃣  The front-end and back-end gets integrated, resulting in a fully functional app that can predict the presence of tuberculosis in the lungs.

## Installation
Firstly Clone the repository locally, then install python version 3.11.2 and download the required libraries using the following command while being in the path of cloned repo.

```bash
pip install -r requirements.txt
```
## To Do
* To enhance the diagnostic capabilities of the application by incorporating support for two additional diseases, namely chronic kidney disease and heart disease.
* To establish a connection between the application and a database to improve data caching and enable efficient retraining of the model.

## Technologies Used
<p align="left" style="display:flex; justify-content: space-between;">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/2d/Tensorflow_logo.svg" width="90">
  <img src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width="180">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/31/NumPy_logo_2020.svg" width="280">
  <img src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width="280">
  <img src="https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg" width="150">
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg" width="150">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg" width="150">
  <img src="https://cms-assets.tutsplus.com/uploads/users/30/posts/16037/preview_image/flask.png" width="150">
</p>

## LICENSE
[GNU](LICENSE.md)
