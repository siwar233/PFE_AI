''' from app import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError


class HR(db.Model):
    __tablename__ = 'hr'
    hr_id = db.Column(db.Integer, primary_key=True)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    jobs = db.relationship('Job', backref='hr', lazy=True)




    @staticmethod
    def add_hr(user_id, first_name, last_name, email, phone_number=None):
        new_hr = HR(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number
        )
        db.session.add(new_hr)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("HR with this email already exists")

    @staticmethod
    def get_hr_by_id(hr_id):
        return HR.query.get(hr_id)

    @staticmethod
    def get_hr_by_email(email):
        return HR.query.filter_by(email=email).first()

    @staticmethod
    def update_hr(hr_id, **kwargs):
        hr = HR.query.get(hr_id)
        if not hr:
            raise ValueError("HR not found")
        for key, value in kwargs.items():
            if hasattr(hr, key):
                setattr(hr, key, value)
        db.session.commit()

    @staticmethod
    def delete_hr(hr_id):
        hr = HR.query.get(hr_id)
        if not hr:
            raise ValueError("HR not found")
        db.session.delete(hr)
        db.session.commit()
'''