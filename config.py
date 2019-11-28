class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://dan:12345@localhost/blog'

    pass

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUD = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}