from flask import Flask
from Project.config import Config
from flask_sqlalchemy import SQLAlchemy
from .models import init_db
from .routes import init_routes

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    
    init_db(app)

    
    init_routes(app)

    return app
