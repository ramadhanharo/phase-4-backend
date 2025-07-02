from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app.models import db
from app.routes.auth_routes import auth_bp
from app.routes.vendor_routes import vendor_bp
from app.routes.review_routes import review_bp

jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:rama123@localhost/locavore_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Replace with secure key in production

    # Initialize extensions
    CORS(app)
    db.init_app(app)
    Migrate(app, db)
    jwt.init_app(app)

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(vendor_bp)
    app.register_blueprint(review_bp)

    # Root route for health check
    @app.route('/')
    def index():
        return jsonify({"message": "Locavore backend is running!"}), 200

    return app
