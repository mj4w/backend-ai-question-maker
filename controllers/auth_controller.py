from flask import Blueprint, request, jsonify
from services.supabase_service import sign_up_user, sign_in_user
from supabase import create_client, Client
from config import Config
supabase: Client = create_client(Config.SUPABASE_URL, Config.SUPABASE_KEY)

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    result = sign_up_user(email, password)

    if "error" in result:
        return jsonify({"error": result["error"]}), 400

    if isinstance(result, object):
        try:
            result = result.to_dict()
        except AttributeError:
            result = dict(result)

    return jsonify(result), 200


@auth_bp.route("/signin", methods=["POST"])
def signin():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if response.user:
            return jsonify({
                "user": {
                    "id": response.user.id,
                    "email": response.user.email,
                },
                "access_token": response.session.access_token,
                "refresh_token": response.session.refresh_token, 
            })
        else:
            return jsonify({"error": "Invalid credentials"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500