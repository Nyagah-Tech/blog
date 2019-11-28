class Config:
    pass

class prodConfig(Config):
    pass

class DevConfig(Config):
    DEBUD = True

config_options = {
    'development' = DevConfig,
    'production' = ProdConfig
}