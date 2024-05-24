

from .register import register_bp
from .login import login_bp

def init_routes(app):
    app.register_blueprint(register_bp)
    app.register_blueprint(login_bp)
