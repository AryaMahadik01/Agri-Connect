from flask import Blueprint, jsonify
from app import mongo

product_bp = Blueprint('products', __name__)

@product_bp.route('/', methods=['GET'])
def get_products():
    products = list(mongo.db.products.find())
    for p in products:
        p['_id'] = str(p['_id'])
    return jsonify(products)
