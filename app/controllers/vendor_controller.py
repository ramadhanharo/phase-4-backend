from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Vendor, User

@jwt_required()
def get_vendors():
    vendors = Vendor.query.all()
    return jsonify([
        {
            "id": v.id,
            "name": v.name,
            "description": v.description,
            "location": v.location,
            "user_id": v.user_id
        } for v in vendors
    ]), 200

@jwt_required()
def get_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    return jsonify({
        "id": vendor.id,
        "name": vendor.name,
        "description": vendor.description,
        "location": vendor.location,
        "user_id": vendor.user_id
    }), 200

@jwt_required()
def create_vendor():
    data = request.get_json()
    current_user = get_jwt_identity()

    name = data.get("name")
    description = data.get("description")
    location = data.get("location")

    if not name or not location:
        return jsonify({"error": "Name and location are required"}), 400

    vendor = Vendor(name=name, description=description, location=location, user_id=current_user)
    db.session.add(vendor)
    db.session.commit()

    return jsonify({
        "id": vendor.id,
        "name": vendor.name,
        "description": vendor.description,
        "location": vendor.location,
        "user_id": vendor.user_id
    }), 201

@jwt_required()
def update_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    current_user = get_jwt_identity()

    if vendor.user_id != current_user:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    vendor.name = data.get("name", vendor.name)
    vendor.description = data.get("description", vendor.description)
    vendor.location = data.get("location", vendor.location)

    db.session.commit()

    return jsonify({
        "id": vendor.id,
        "name": vendor.name,
        "description": vendor.description,
        "location": vendor.location
    }), 200

@jwt_required()
def delete_vendor(id):
    vendor = Vendor.query.get_or_404(id)
    current_user = get_jwt_identity()

    if vendor.user_id != current_user:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(vendor)
    db.session.commit()
    return jsonify({"message": "Vendor deleted"}), 200
