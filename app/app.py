from flask import Flask
from config import Config
from app.models.user import db
from .routes import register_bp, login_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from .models import User  

    # Register blueprints
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)

    return app
