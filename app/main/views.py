from flask import render_template
from . import main


#views
@main.route('/')
def index():
    '''
    view root function that return the index page and its data
    '''
    render_template('index.html')