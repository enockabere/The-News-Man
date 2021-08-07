class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
class prodConfig(Config):
    '''
    Production Configuration Child Class
    '''
    '''
    Args:
        Config:It inherits from the parent configuration class with the general configurations
    '''
    pass
class DevConfig(Config):
    '''
    Development Configuration Child Class
    Args:
        Config:It inherits from the parent configuration class with the general configurations
    '''
    DEBUG = True