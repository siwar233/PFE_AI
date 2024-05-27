from datetime import datetime
from app import db
from sqlalchemy.exc import IntegrityError


class Resume(db.Model):
    __tablename__ = 'resumes'
    resume_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    resume_file = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    parsed_date = db.Column(db.DateTime)


    @staticmethod
    def add_resume(candidate_id, resume_file, parsed_date=None):
        new_resume = Resume(
            candidate_id=candidate_id,
            resume_file=resume_file,
            parsed_date=parsed_date
        )
        db.session.add(new_resume)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the resume")

    @staticmethod
    def get_resume_by_id(resume_id):
        return Resume.query.get(resume_id)

    @staticmethod
    def get_resumes_by_candidate_id(candidate_id):
        return Resume.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_resume(resume_id, **kwargs):
        resume = Resume.query.get(resume_id)
        if not resume:
            raise ValueError("Resume not found")
        for key, value in kwargs.items():
            if hasattr(resume, key):
                setattr(resume, key, value)
        db.session.commit()

    @staticmethod
    def delete_resume(resume_id):
        resume = Resume.query.get(resume_id)
        if not resume:
            raise ValueError("Resume not found")
        db.session.delete(resume)
        db.session.commit()