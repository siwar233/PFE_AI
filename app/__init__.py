from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .models import init_db
    init_db(app)

    from .routes import init_routes
    init_routes(app)

    return app
