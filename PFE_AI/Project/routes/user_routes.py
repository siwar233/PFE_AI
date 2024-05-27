from flask import Blueprint, request, jsonify, render_template
from Project.services.user_service import create_user, get_user_by_username
from Project.models.user import  User

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    
    if get_user_by_username(username):
        return jsonify({'message': 'User already exists'}), 400
    
    user = create_user(username, email, password)
    return jsonify({'message': 'User created successfully'}), 201

@user_bp.route('/signin', methods=['POST'])
def signin():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    user = get_user_by_username(username)
    if user and user.check_password(password):
        return jsonify({'message': 'Signed in successfully'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@user_bp.route('/')
def index():
    return render_template('index.html')
