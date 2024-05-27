from flask import Blueprint

def init_routes(app):
    from .user_routes import user_bp
    from .
    app.register_blueprint(user_bp)
