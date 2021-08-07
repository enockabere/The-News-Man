class Config:
    '''
    General configuration parent class
    '''
    pass
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