from src.apps.main import main

@main.route('/')
def index():
    return "hello world"
