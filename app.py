from flask import Flask
from flask_cors import CORS
import os
from config import Config

# Controllers
from controllers.upload_controller import upload_bp
from controllers.auth_controller import auth_bp

def create_app():
    app = Flask(__name__)

    # Load Config
    app.config.from_object(Config)

    # Enable CORS (allow frontend requests)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Ensure upload folder exists
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(upload_bp, url_prefix="/upload")

    @app.route("/")
    def home():
        return {"message": "AI Question Maker Flask API is running."}

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
