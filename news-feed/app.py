#!/usr/bin/python3
import os
from flask import Flask, render_template, url_for
from werkzeug.utils import secure_filename

image = os.path.join('static', 'images')

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = image

@app.route('/index/')
def index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'index.jpg')
    #return render_template("index.html", user_image = full_filename)
    return render_template("index.html")

@app.route('/hello')
def hello():
    return "hello world test; it can me the landing page // WIP"

@app.route('/about/')
def about():
    return "just the about page // WIP"

