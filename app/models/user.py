from datetime import datetime
from app import db
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    candidates = db.relationship('Candidate', backref='user', lazy=True)
    #    def __repr__(self):
    #     return f'<User {self.username}>'

    # @staticmethod
    # def add_user(username, email, password):
    #     new_user = User(username=username, email=email, password=password)
    #     db.session.add(new_user)
    #     try:
    #         db.session.commit()
    #     except IntegrityError:
    #         db.session.rollback()
    #         raise ValueError("User with this username or email already exists")

    # @staticmethod
    # def get_user_by_id(user_id):
    #     return User.query.get(user_id)

    # @staticmethod
    # def get_user_by_username(username):
    #     return User.query.filter_by(username=username).first()

    # @staticmethod
    # def update_user(user_id, **kwargs):
    #     user = User.query.get(user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #     for key, value in kwargs.items():
    #         if hasattr(user, key):
    #             setattr(user, key, value)
    #     db.session.commit()

    # @staticmethod
    # def delete_user(user_id):
    #     user = User.query.get(user_id)
    #     if not user:
    #         raise ValueError("User not found")
    #     db.session.delete(user)
    #     db.session.commit()