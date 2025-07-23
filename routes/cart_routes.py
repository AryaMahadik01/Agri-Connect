from flask import Blueprint, request, jsonify
from app import mongo

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/<user_id>', methods=['GET'])
def get_cart(user_id):
    user = mongo.db.users.find_one({"_id": user_id})
    return jsonify(user.get("cart", []))


@cart_bp.route('/add', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    mongo.db.users.update_one(
        {"_id": data['user_id']},
        {"$push": {"cart": data['product']}}
    )
    return jsonify({"message": "Product added to cart"})


@cart_bp.route('/remove', methods=['POST'])
def remove_from_cart():
    data = request.get_json()
    mongo.db.users.update_one(
        {"_id": data['user_id']},
        {"$pull": {"cart": {"product_id": data['product_id']}}}
    )
    return jsonify({"message": "Product removed from cart"})
