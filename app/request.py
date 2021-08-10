import urllib.request
import json
from .models import NewsSource
from .models import Articles


#Fetch API key
api_key = None

#Fetch News Base Url
base_url = None
article_url = None
def configure_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    article_url = app.config['ARTICLES_API_BASE_URL']
def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(api_key)
    
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        
        sources_result = None
        
        if get_sources_response['sources']:
            sources_result_list = get_sources_response['sources']
            sources_result = process_results(sources_result_list)
    return sources_result
def process_results(sources_list):
    '''
    Function that processes the news sources result and transform them to a list of objects
    Args:
        sources_list: a list of dictionaries that contain news sources details
    Returns:
        sources_result: a list of news sources objects
    '''
    sources_result = []
    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')
        if url:
            sources_object = NewsSource(id,name,description,url,category,language,country)
            sources_result.append(sources_object)
    return sources_result
#Article Functions
def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = article_url.format(category,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
        articles_results = None
        if get_articles_response ['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = art_results (articles_results_list)
    return articles_results
def art_results(article_list):
        '''
        Function that processes the news articles result and transform them to a list of objects
        Args:
            article_list: a list of dictionaries that contain news articles details
        Returns:
            articles_result: a list of news articles objects
        '''
        articles_results = []
        for article_item in article_list:
            author = article_item.get('author')
            title = article_item.get('title')
            description = article_item.get('description')
            url = article_item.get('url')
            urlToImage = article_item.get('urlToImage')
            publishedAt = article_item.get('publishedAt')
            content = article_item.get('content')
            
            if urlToImage:
                articles_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
                articles_results.append(articles_object)
        return articles_results
def get_art(title):
    get_art_details_url = article_url.format(title,api_key)
    
    with urllib.request.urlopen(get_art_details_url) as url:
        art_details_data = url.read()
        art_details_response = json.loads(art_details_data)
        
        art_object = None
        
        if art_details_response:
            author = art_details_response.get('author')
            title = art_details_response.get('title')
            description = art_details_response.get('description')
            url = art_details_response.get('url')
            urlToImage = art_details_response.get('urlToImage')
            publishedAt = art_details_response.get('publishedAt')
            content = art_details_response.get('content')
            
            art_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
    return art_object
def search_article(article_name):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&sortBy=popularity&apiKey={}'.format(article_name,api_key)
    with urllib.request.urlopen(search_article_url) as url:
        search_article_data = url.read()
        search_article_response = json.loads(search_article_data)
        
        search_article_results = None
        
        if search_article_response ['articles']:
            search_article_list = search_article_response['articles']
            search_article_results = art_results(search_article_list)
    return search_article_results

    
        