from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    """
    :return app: Flask app
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= 'mysql://root:@localhost/oculi'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # Limit to 16 MB, adjust as needed
    app.json.sort_keys = False
    app.secret_key = 'Oculi'

    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)

    # from .models import Users
    from app.controllers import api
    app.register_blueprint(api, url_prefix="/api")

    return app
