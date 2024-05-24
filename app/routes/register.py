from flask import Blueprint, render_template, request, redirect, url_for,flash
from app.models.user import User,db

register_bp = Blueprint('register', __name__)
@register_bp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        First_name = request.form['First_name']
        Last_name = request.form['Last_name']
        username = request.form['Username']
        phone = request.form['Phone']
        email = request.form['Email']
        password = request.form['Password']

        try:
            new_user = User.add_user(First_name, Last_name, username, phone, email, password)
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful! Please log in.", "success")
          
        except ValueError as e:
            flash(str(e), "danger")
    return render_template('sign_up.html')
    