from flask import Flask, render_template, request
import json

# Initialize Flask Application
app = Flask(__name__)

# App home screen
@app.route('/app')
def hello_world():
    return render_template('app.html')
