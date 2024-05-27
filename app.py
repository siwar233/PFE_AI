from flask import Flask
from Project.config import Config
from Project.models import init_db
from Project.routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    init_db(app)
    
    init_routes(app)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
