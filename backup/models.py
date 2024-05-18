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

    @staticmethod
    def user_signup(First_name, Last_name, Username, Age, Phone, Email, Password):
        hashed_password = generate_password_hash(Password)

        new_user = User(
            First_name=First_name,
            Last_name=Last_name,
            Username=Username,
            Age=Age,
            Phone=Phone,
            Email=Email,
            Password=hashed_password
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user

class HR_Accounts(db.Model):
    __tablename__ = 'HR_Accounts'
    Account_id = db.Column(db.BigInteger, primary_key=True)
    First_name = db.Column(db.String(255))
    Last_name = db.Column(db.String(255))
    Username = db.Column(db.String(255))
    Age = db.Column(db.Date)
    Phone = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Password = db.Column(db.String(255))

class JobPosting(db.Model):
    __tablename__ = 'job_posting'
    job_id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(255))
    uploaded_by = db.Column(db.BigInteger, db.ForeignKey('HR_Accounts.Account_id'))
