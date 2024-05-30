from Project.models.user import User
from Project.models import db
from sqlalchemy.exc import IntegrityError

def create_user(first_name, last_name, email, username, password):
    user = User(first_name=first_name, last_name=last_name, email=email, username=username, password=password)
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise ValueError("User with this email or username already exists")
    return user

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

try:
        # Create all tables
        db.create_all()

        # Perform a simple query to check the connection
        users = User.query.all()
        print("Database connection successful!")
except Exception as e:
        print("Database connection failed:", e)

