from flask import Flask
from flask_cors import CORS
import os
from config import Config
from controllers.upload_controller import upload_bp

def create_app():
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER
    CORS(app)

    # Create upload folder if not exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Register blueprints
    app.register_blueprint(upload_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
