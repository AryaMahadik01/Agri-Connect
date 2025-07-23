from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from app import mongo
import uuid

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data['email']
    password = generate_password_hash(data['password'])

    if mongo.db.users.find_one({"email": email}):
        return jsonify({"message": "User already exists"}), 409

    mongo.db.users.insert_one({
        "_id": str(uuid.uuid4()),
        "name": data['name'],
        "email": email,
        "password": password,
        "cart": [],
        "wishlist": []
    })
    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = mongo.db.users.find_one({"email": data['email']})

    if user and check_password_hash(user['password'], data['password']):
        return jsonify({"message": "Login successful", "user_id": user['_id']})
    return jsonify({"message": "Invalid credentials"}), 401
