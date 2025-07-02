from datetime import datetime
from app import db  # ✅ Import the already-initialized db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    vendors = db.relationship("Vendor", backref="user", cascade="all, delete")
    reviews = db.relationship("Review", backref="user", cascade="all, delete")

class Vendor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    location = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    reviews = db.relationship("Review", backref="vendor", cascade="all, delete")

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    vendor_id = db.Column(db.Integer, db.ForeignKey("vendor.id"))
