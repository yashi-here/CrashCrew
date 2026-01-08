from flask import Flask
from config import Config
from models import db
from routes.auth import auth_bp
from routes.profile import profile_bp
from routes.dashboard import dashboard_bp
from flask_jwt_extended import JWTManager
import os

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    JWTManager(app)

    # Ensure instance folder exists
    os.makedirs(os.path.join(app.root_path, "instance"), exist_ok=True)

    db.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    
    app.register_blueprint(profile_bp, url_prefix="/api/profile")

    app.register_blueprint(dashboard_bp, url_prefix="/api/dashboard")


    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return {"status": "Backend + DB running successfully"}

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
