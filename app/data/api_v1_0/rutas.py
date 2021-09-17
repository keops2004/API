from . import auth_bp
#from app.data.api_v1_0.decorador import jwt_required
from flask_jwt_extended import create_access_token,jwt_required, get_jwt_identity


@app.route("/token", methods=["POST"])
def create_token():
    password = request.json.get("password", None)
    access_token = create_access_token(identity=password)
    return jsonify({ "token": access_token, "password": password })


 
