from datetime import datetime
from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
from app import db
from models import User

def sign_up_user(first_name, last_name, username, email, password, role):
    """
    Handle user registration by creating a new user record.
    """
    if not all([first_name, last_name, username, email, password, role]):
        raise ValueError("All fields are required!")
    
    hashed_password = generate_password_hash(password, method='sha256')
    
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=hashed_password,
        role=role,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully!"}
    except IntegrityError as e:
        db.session.rollback()
        raise ValueError(f"User could not be created: {e}")
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"An error occurred: {e}")

def sign_in_user(username, password):
    """
    Authenticate user and manage session.
    """
    if not all([username, password]):
        raise ValueError("Username and password are required!")
    
    user = User.query.filter_by(username=username).first()
    
    if user and check_password_hash(user.password, password):
        session['user_id'] = user.user_id
        session['username'] = user.username
        session['role'] = user.role
        return {"message": "Login successful!"}
    else:
        raise ValueError("Invalid username or password!")

def sign_out_user():
    """
    Handle user logout by clearing the session.
    """
    session.clear()
    return {"message": "Logout successful!"}

def get_user_info(user_id):
    #user personal info
    user = User.get_user_by_id(user_id)
    return user

if User:
    print(f"First Name: {User.First_name}")
    print(f"Last Name: {User.Last_name}")
    print(f"Phone: {User.Phone}")  
    print(f"Username: {User.username}")
    print(f"Email: {User.email}")
    print(f"Role: {User.role}")  
    print(f"Password: {User.password}")  
    print(f"Created at: {User.created_at}") 
    print(f"Updated at: {User.updated_at}")  
    print("User not found.")