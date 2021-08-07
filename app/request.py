from os import name
from app import app
import urllib.request,json
from . models import source

News_source = source.News_Source


#Fetch API key
api_key = app.config['MOVIE_API_KEY']

#Fetch News Base Url
base_url = app.config["NEWS_API_BASE_URL"]
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
            sources_object = News_source(id,name,description,url,category,language,country)
            sources_result.append(sources_object)
    return sources_result
    