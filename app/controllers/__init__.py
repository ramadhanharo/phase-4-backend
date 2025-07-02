from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import os
from dotenv import load_dotenv

from app.models import db
from app.routes.vendor_routes import vendor_bp
from app.routes.review_routes import review_bp

load_dotenv()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Load configuration from .env or Render environment
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(vendor_bp)
    app.register_blueprint(review_bp)

    # Health check route
    @app.route('/')
    def index():
        return jsonify({"message": "Locavore backend is running!"}), 200

    return app
