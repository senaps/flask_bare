import click

from flask.cli import FlaskGroup
from src.application import create_app
from src.configs import DevelopmentConfig

def _app():
    app = create_app(DevelopmentConfig)
    
app = create_app(DevelopmentConfig)

@click.command(cls=FlaskGroup, create_app=_app)
def cli():
    """this initializes the code for us """


if __name__ == '__main__':
    cli()
