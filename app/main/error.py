from flask import render_template
from app import app

@app.errorhandler(404)
def fourError(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('fourError.html'),404