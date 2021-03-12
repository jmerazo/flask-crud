from flask import Flask, render_template

app = Flask(__name__, template_folder='views')

from src.controllers import *

def start_app():
    app.run(port = 3000, debug=True)