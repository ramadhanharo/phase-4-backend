from flask import Blueprint
from flask_jwt_extended import jwt_required
from app.controllers.review_controller import create_review, update_review, delete_review

review_bp = Blueprint('review_bp', __name__)

# Create a review for a vendor
@review_bp.route('/vendors/<int:vendor_id>/reviews/', methods=['POST'])
@jwt_required()
def handle_create_review(vendor_id):
    return create_review(vendor_id)

# Update a review by its ID
@review_bp.route('/reviews/<int:id>/', methods=['PATCH'])
@jwt_required()
def handle_update_review(id):
    return update_review(id)

# Delete a review by its ID
@review_bp.route('/reviews/<int:id>/', methods=['DELETE'])
@jwt_required()
def handle_delete_review(id):
    return delete_review(id)
