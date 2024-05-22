from models import User, db
from sqlalchemy.exc import IntegrityError
from models import User

 
 
def get_user_info(user_id):
    #user personal info
    user = User.get_user_by_id(user_id)
    return user

if User:
        # Display user information on the page
        print(f"Username: {User.username}")
        print(f"Email: {User.email}")
        print(f"Role: {User.role}")
        print(f"Created at: {User.created_at}")
        print(f"Updated at: {User.updated_at}")
else:
        print("User not found.")
