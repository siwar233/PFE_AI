from flask import Blueprint, request, jsonify, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from models import User
from datetime import datetime
from flask import render_template, session, redirect, url_for, request 
from services.user_service import get_user_info


user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    role = data.get('role')
    
    if not all([first_name, last_name, username, email, password, role]):
        return jsonify({"message": "All fields are required!"}), 400
    
    hashed_password = generate_password_hash(password, method='sha256')
    
    new_user = User(
        username=username,
        password=hashed_password,
        email=email,
        role=role,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User created successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "User could not be created!", "error": str(e)}), 500
    

#!!!!!!!

@user_bp.route('/home', methods=['POST'])
def signin():
    data = request.get_json()
    
    username = data.get('username')
    password = data.get('password')
    
    if not all([username, password]):
        return jsonify({"message": "Username and password are required!"}), 400
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.user_id
        session['username'] = user.username
        session['role'] = user.role
        return jsonify({"message": "Login successful!"}), 200
    else:
        return jsonify({"message": "Invalid username or password!"}), 401

@user_bp.route('/home_page', methods=['POST'])
def signout():
    session.clear()
    return jsonify({"message": "Logout successful!"}), 200

#user personl info
@user_bp.route('/personal_info')
def display_personal_info():
    """
    Display user's personal information.
    """
    # Check if user is logged in
    if 'user_id' not in session:
        return redirect(url_for('login'))  
    
    # Retrieve user ID from session
    user_id = session['user_id']
    
    # Retrieve user information
    user = get_user_info(user_id)
    
    if user:
        return render_template('personal_info.html', user=user)
    else:
        return "User not found."

