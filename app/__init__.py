from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from config import Config
from app.utils.auth import bcrypt

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.vendor_routes import vendor_bp
    from app.routes.review_routes import review_bp

    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(vendor_bp, url_prefix="/vendors")
    app.register_blueprint(review_bp, url_prefix="/reviews")

    return app

