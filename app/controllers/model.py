from flask import Blueprint, jsonify, request

bp = Blueprint('model', __name__)

@bp.route("/test", methods=['GET'])
def test():

    return jsonify({"success:": True,
                    "message": "Endpoint Working"}), 200


@bp.route("/extract-text", methods=['POST'])
def extract_text():
    data = request.get_json()
    
    if data:
        return jsonify({"success": True,
                        "data": data})

    else:
        return jsonify({"success": False,
                        "message": "No JSON data provided"}), 400
