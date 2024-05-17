from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'HR accounts'
    Account_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    First_name = db.Column(db.String(255), nullable=False)
    Last_name = db.Column(db.String(255), nullable=False)
    Username = db.Column(db.String(255), unique=True, nullable=False)
    Age = db.Column(db.Date, nullable=False)
    Phone = db.Column(db.String(255), nullable=False)
    Email = db.Column(db.String(255), unique=True, nullable=False)
    Password = db.Column(db.String(255), nullable=False)

    def user_signup(First_name, Last_name, Username, Age, Phone, Email, Password):
        hashed_password = generate_password_hash(Password)

        new_user = User(
            First_name = First_name,
            Last_name = Last_name,
            Username = Username,
            Age = Age,
            Phone = Phone,
            Email = Email,
            Password = hashed_password
        )

        db.session.add(new_user)

        db.session.commit()

        return new_user