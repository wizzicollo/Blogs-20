import os

class Config:
    '''
    general configuration parent class
    '''
    SECRET_KEY= os.environ.get('SECRET_KEY')
    QUOTES_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    # SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collins:qwertyui@localhost/bloggers'

class ProdConfig(Config):
    '''
    Pruduction configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    '''
    Testing configuration child class
    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://collins:qwertyui@localhost/blogging'

    DEBUG=True

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}