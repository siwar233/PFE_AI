'''
from app import db
from models import HR
from sqlalchemy.exc import IntegrityError

def create_hr(first_name, last_name, email, phone_number=None, user_id=None):
  
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

def update_hr(hr_id, **kwargs):
   
    hr = HR.query.get(hr_id)
    if not hr:
        raise ValueError("HR not found")
    for key, value in kwargs.items():
        if hasattr(hr, key):
            setattr(hr, key, value)
    db.session.commit()
'''

