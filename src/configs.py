class DefaultConfig:
    DEBUG = True
    TESTING = False
    PORT = 7000

class DevelopmentConfig(DefaultConfig):
    pass

class ProductionConfig(DefaultConfig):
    DEBUG = False

class TestingConfig(DefaultConfig):
    TESTING = True
