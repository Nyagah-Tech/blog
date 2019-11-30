class Config:

    SECRET_KEY ='dm/01254'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:12345@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}