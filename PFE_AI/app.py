from flask import Flask, render_template
from Project.config import Config
from Project.models import db, init_db
from Project.routes import init_routes

def create_app():
    app = Flask(__name__, template_folder='Project/templates')
    app.config.from_object(Config)
    
    init_db(app)
    init_routes(app)  # Initialize routes and register blueprints

    @app.route('/')
    def home():
        return render_template('home.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)
