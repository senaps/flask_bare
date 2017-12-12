from flask import Flask


def create_app(config):
    app = Flask(__name__)
    _load_config(app, config)
    _load_blueprints(app)

    return app


def _load_config(app, config):
    """load up the configuration settings for the app

    this will load the given configuration class while
    creating the app
    """
    app.config.from_object(config)

    
def _load_blueprints(app):
    """load the blueprints for the app

    import the blueprints, register them in this function
    and they are useable for the app
    """
    from src.apps.main import main

    app.register_blueprint(main)
