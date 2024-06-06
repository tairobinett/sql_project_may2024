from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world(): 
    return "<p>Hello World!</p>"

@app.route("/gb")
def gb_world(): 
    return "<p>Goodbye World!</p>"
