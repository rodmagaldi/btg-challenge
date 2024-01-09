from flask import Flask
from flask_cors import CORS

from .main import main as main_blueprint

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(main_blueprint)

    return app
