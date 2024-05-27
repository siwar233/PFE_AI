from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from app.models.user import User
from app.services.user_service import sign_in_user

login_bp = Blueprint('home', __name__)

@login_bp.route('/', methods=['GET', 'POST'])
def home_page():
    """Route to redirect to the home page."""
    return redirect(url_for('home.home'))

@login_bp.route('/home', methods=['GET', 'POST'])
def login():
    """Route for user login."""
    if request.method == 'GET':
        # Render the login form
        return render_template("home.html")
    elif request.method == 'POST':
        # Process login data
        try:
            email = request.form.get("Email")  
            password = request.form.get("Password")

            user = sign_in_user.authenticate_user(email, password)
            if user:
                session['user_id'] = user.user_id
                flash(f"Welcome, {user.username}!", "success")
                # Redirect to job application page after successful login
                return redirect(url_for('home.JobApp'))
            else:
                flash("Invalid email or password", "danger")
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "danger")
          
    else:
        # Handle other HTTP methods, return a 405 error
        return "Method Not Allowed", 405

@login_bp.route('/job_app')
def job_app():
    """Route for the job application page."""
    user_id = session.get('user_id')
    if not user_id:
        flash("Please sign in first", "warning")
        return redirect(url_for('home.home'))
    
    user = User.get_user_by_id(user_id)
    if user:
        return f"Welcome, {user.username}! Email: {user.email}"
    else:
        flash("User not found", "danger")
        return redirect(url_for('home.home'))
