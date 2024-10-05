from flask import render_template
from . import homeBlu
@homeBlu.route('/')
def home():
    return render_template('index.html')