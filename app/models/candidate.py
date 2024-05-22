from datetime import datetime
from app import db
from sqlalchemy.exc import IntegrityError



class Candidate(db.Model):
    __tablename__ = 'candidates'
    candidate_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(200))
    date_of_birth = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    resumes = db.relationship('Resume', backref='candidate', lazy=True)
    experiences = db.relationship('Experience', backref='candidate', lazy=True)
    educations = db.relationship('Education', backref='candidate', lazy=True)
    candidate_skills = db.relationship('CandidateSkill', backref='candidate', lazy=True)
    certifications = db.relationship('Certification', backref='candidate', lazy=True)
    projects = db.relationship('Project', backref='candidate', lazy=True)
    candidate_languages = db.relationship('CandidateLanguage', backref='candidate', lazy=True)


    @staticmethod
    def add_candidate(user_id, first_name, last_name, email, phone_number=None, address=None, date_of_birth=None):
        new_candidate = Candidate(
            user_id=user_id, 
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone_number=phone_number, 
            address=address, 
            date_of_birth=date_of_birth
        )
        db.session.add(new_candidate)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Candidate with this email already exists")

    @staticmethod
    def get_candidate_by_id(candidate_id):
        return Candidate.query.get(candidate_id)

    @staticmethod
    def get_candidate_by_email(email):
        return Candidate.query.filter_by(email=email).first()

    @staticmethod
    def update_candidate(candidate_id, **kwargs):
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            raise ValueError("Candidate not found")
        for key, value in kwargs.items():
            if hasattr(candidate, key):
                setattr(candidate, key, value)
        db.session.commit()

    @staticmethod
    def delete_candidate(candidate_id):
        candidate = Candidate.query.get(candidate_id)
        if not candidate:
            raise ValueError("Candidate not found")
        db.session.delete(candidate)
        db.session.commit()
