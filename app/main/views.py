from flask import render_template, request, redirect,url_for
from app import app
from .request import get_sources, get_articles, search_article,get_art

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    data = {
        "title":"The News Man",
        "heading": "News Man", 
    }
    sources = get_sources()
    print(sources)
    articles = get_articles('omosh')
    print(articles)
    search_article = request.args.get('article_query')
    if search_article:
        return redirect(url_for('search',article_name=search_article))
    else:
        return render_template('index.html', context=data,sources= sources,omosh=articles)
@app.route('/articles/<string:title>')
def articles(title):
    '''
    it shows the news articles from the selected sources
    '''
    articles = get_art(title).replace(" ","-").lowercase()
    return render_template('articles.html',articles=articles)
@app.route('/search/<article_name>')
def search(article_name):
    '''
    View function to display the search results
    '''
    article_name_list = article_name.split(" ")
    article_name_format = "+".join(article_name_list)
    searched_articles = search_article(article_name_format)
    title = f'search results for {article_name}'
    return render_template('search.html',articles = searched_articles)