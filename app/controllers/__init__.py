from flask import Blueprint

api = Blueprint('api', __name__)

from . import model, auth

api.register_blueprint(model.bp, url_prefix="/model")
api.register_blueprint(auth.bp, url_prefix="/auth")