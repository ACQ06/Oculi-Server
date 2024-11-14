from flask import Blueprint, jsonify, request
from ..models import Admin

bp = Blueprint('auth', __name__)

@bp.route("/test", methods=['GET'])
def test():
    return jsonify({"success:": True,
                    "message": "Endpoint Working"}), 200

def signin():
    pass

def signout():
    pass

@bp.route("/signup", methods=['POST'])
def signup():
    credentials = request.get_json()
    if not request.is_json:
        return jsonify({"success": False, "message": "Request must be in JSON format"}), 400

    if not credentials:
        return jsonify({"success": False, 'message': 'No JSON data provided'}), 400

    if 'username' not in credentials or 'password' not in credentials:
        return jsonify({"success": False, 'message': 'Missing username or password'}), 400
    
    username = credentials["username"]
    password = credentials["password"]

    try:
        data = Admin.create_admin(username=username, password=password)

        return jsonify({"success": True,
                        "message": "Sign Up Successfully",
                        "data": data})

    except Exception as e:
        return jsonify({"success": True,
                        "message": e})

