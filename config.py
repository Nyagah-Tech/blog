class Config:

    SECRET_KEY ='dm/01254'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:12345@localhost/blog'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'danmuv12@gmail.com'
    MAIL_PASSWORD = 'Dm17/01254'
    
    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}