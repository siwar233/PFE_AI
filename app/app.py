from flask import Flask
from models import db
from routes.route_user import user_bp
from routes.uploadresumes import upload_bp
from config import config
import os

app = Flask(__name__)

# Load configuration from config.py
config_name = os.getenv('FLASK_CONFIG') or 'default'
app.config.from_object(config[config_name])

db.init_app(app)

app.register_blueprint(user_bp, url_prefix='/user')
app.register_blueprint(upload_bp, url_prefix='/resume')

if __name__ == '__main__':
    app.run()
