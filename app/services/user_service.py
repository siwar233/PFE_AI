from models import User, db
from sqlalchemy.exc import IntegrityError

class UserService:

    @staticmethod
    def create_user(username, email, password):
        try:
            User.add_user(username, email, password)
            return {"message": "User created successfully"}, 201
        except ValueError as e:
            return {"error": str(e)}, 400