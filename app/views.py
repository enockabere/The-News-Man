from flask import render_template
from app import app
from .request import get_sources

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    data = {
        "title":"The News Man",
        "heading": "The News Man", 
    }
    sources = get_sources()
    print(sources)
    return render_template('index.html', context=data,sources= sources)
@app.route('/articles/<int:articles_id>')
def articles(articles_id):
    '''
    it shows the news articles from the selected sources
    '''
    return render_template('articles.html',id=articles_id)