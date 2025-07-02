from flask import Blueprint
from app.controllers.vendor_controller import (
    get_vendors, get_vendor, create_vendor,
    update_vendor, delete_vendor
)

vendor_bp = Blueprint("vendor", __name__)

@vendor_bp.route("/", methods=["GET"])
def list_vendors():
    return get_vendors()

@vendor_bp.route("/<int:id>", methods=["GET"])
def vendor_detail(id):
    return get_vendor(id)

@vendor_bp.route("/", methods=["POST"])
def add_vendor():
    return create_vendor()

@vendor_bp.route("/<int:id>", methods=["PUT"])
def edit_vendor(id):
    return update_vendor(id)

@vendor_bp.route("/<int:id>", methods=["DELETE"])
def remove_vendor(id):
    return delete_vendor(id)
