from flask import Flask
from app.views import main


def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    app.register_blueprint(main)

    return app
