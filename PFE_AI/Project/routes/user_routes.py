# Project/routes/user_routes.py
import os
import sys

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

print("Current working directory:", os.getcwd())
print("sys.path:", sys.path)

try:
    from Project.models.user import User, db
    print("Import successful!")
except ModuleNotFoundError as e:
    print(f"ModuleNotFoundError: {e}")
except Exception as e:
    print(f"Other Exception: {e}")

from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from Project.services.user_service import create_user, get_user_by_username, get_user_by_email

user_bp = Blueprint('user', __name__)

@user_bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('First_name')
        last_name = request.form.get('Last_name')
        email = request.form.get('Email')
        username = request.form.get('Username')
        password = request.form.get('Password')

        if not all([first_name, last_name, email, username, password]):
            flash("All fields are required.", "danger")
            return redirect(url_for('user.sign_up'))

        try:
            if get_user_by_email(email) or get_user_by_username(username):
                raise ValueError("Email or username already exists.")
            create_user(first_name, last_name, email, username, password)
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('user.home'))
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for('user.sign_up'))

    return render_template('signup.html')

@user_bp.route('/signin', methods=['GET', 'POST'])
def sign_in():
    if request.method == 'POST':
        email = request.form.get('Email')
        password = request.form.get('Password')

        user = get_user_by_email(email)
        if user and user.check_password(password):
            flash("Signed in successfully", "success")
            return redirect(url_for('user.JobApp'))
        else:
            flash("Invalid credentials", "danger")
            return redirect(url_for('user.home'))

    return render_template('signin.html')

@user_bp.route('/')
def index():
    return render_template('home.html')
