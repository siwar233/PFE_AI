'''
from flask import Blueprint, render_template, request, redirect, url_for, flash
from Project.models.user import User, db

register_bp = Blueprint('register', __name__)

@register_bp.route('/signup', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        First_name = request.form.get('First_name')
        Last_name = request.form.get('Last_name')
        username = request.form.get('Username')
        phone = request.form.get('Phone')
        email = request.form.get('Email')
        password = request.form.get('Password')

        if not all([First_name, Last_name, username, phone, email, password]):
            flash("All fields are required.", "danger")
            return redirect(url_for('register.sign_up'))

        try:
            if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
                raise ValueError("Email or username already exists.")
            new_user = User(username=username, email=email)
            new_user.password = password  # If you are using password hashing, otherwise store directly
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('user_routes.home'))  # Assuming you have a login route
        except ValueError as e:
            flash(str(e), "danger")
            return redirect(url_for('register.sign_up'))

    return render_template('signup.html')  # Ensure this matches your actual file name
'''