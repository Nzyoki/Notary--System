from flask import Flask
from app.routes.auth import auth_bp
from app.routes.document import document_bp
from app.routes.notary import notary_bp
from app.models import db, migrate
import os

def create_app():
    app = Flask(_name_, static_folder='app/static', template_folder='app/templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:////tmp/site.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-fallback')

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(document_bp, url_prefix='/document')
    app.register_blueprint(notary_bp, url_prefix='/notary')

    # Index route
    @app.route('/')
    def index():
        return 'Welcome to the Notary System'

    return app

app = create_app()