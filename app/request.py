from app.models.news_source_test import News_source
from app import app
import urllib.request,json
from .models import news_source

News_source = news_source.News_Source


#Fetch API key
api_key = app.config['NEWS_API_KEY']

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