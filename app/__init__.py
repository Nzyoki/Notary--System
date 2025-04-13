from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import Config
import os

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

   
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'


    from app.models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    
    from app.routes import auth, document, notary
    app.register_blueprint(auth.bp)
    app.register_blueprint(document.bp)
    app.register_blueprint(notary.bp)

    with app.app_context():
        db.create_all()

    return app