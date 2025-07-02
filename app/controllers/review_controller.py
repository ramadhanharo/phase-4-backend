from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Review, Vendor

@jwt_required()
def create_review(vendor_id):
    data = request.get_json()
    content = data.get("content")
    rating = data.get("rating")
    user_id = get_jwt_identity()

    if not content or not rating:
        return jsonify({"error": "Content and rating are required"}), 400

    vendor = Vendor.query.get(vendor_id)
    if not vendor:
        return jsonify({"error": "Vendor not found"}), 404

    review = Review(content=content, rating=rating, vendor_id=vendor_id, user_id=user_id)
    db.session.add(review)
    db.session.commit()

    return jsonify({
        "id": review.id,
        "content": review.content,
        "rating": review.rating,
        "vendor_id": review.vendor_id,
        "user_id": review.user_id
    }), 201

@jwt_required()
def update_review(id):
    review = Review.query.get_or_404(id)
    current_user = get_jwt_identity()

    if review.user_id != current_user:
        return jsonify({"error": "Unauthorized"}), 403

    data = request.get_json()
    review.content = data.get("content", review.content)
    review.rating = data.get("rating", review.rating)

    db.session.commit()

    return jsonify({
        "id": review.id,
        "content": review.content,
        "rating": review.rating
    }), 200

@jwt_required()
def delete_review(id):
    review = Review.query.get_or_404(id)
    current_user = get_jwt_identity()

    if review.user_id != current_user:
        return jsonify({"error": "Unauthorized"}), 403

    db.session.delete(review)
    db.session.commit()

    return jsonify({"message": "Review deleted"}), 200
