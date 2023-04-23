from flask import Flask, redirect, url_for, render_template, request, make_response
from flask import send_from_directory
from pygryphon import greet
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/hello", methods=['GET'])
def hello():
    return greet.hello('User')


@app.route("/gryphon.png", methods=['GET'])
def serving_files():
    return send_from_directory('static', 'gryphon.png')
