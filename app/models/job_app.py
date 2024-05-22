from datetime import datetime
from app import db
from sqlalchemy.exc import IntegrityError


class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    job_application_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)
    application_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='Pending')


    @staticmethod
    def add_job_application(candidate_id, job_id, status='Pending'):
        new_application = JobApplication(
            candidate_id=candidate_id,
            job_id=job_id,
            status=status
        )
        db.session.add(new_application)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the job application")

    @staticmethod
    def get_job_application_by_id(job_application_id):
        return JobApplication.query.get(job_application_id)

    @staticmethod
    def get_job_applications_by_candidate_id(candidate_id):
        return JobApplication.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_job_application(job_application_id, **kwargs):
        job_application = JobApplication.query.get(job_application_id)
        if not job_application:
            raise ValueError("Job application not found")
        for key, value in kwargs.items():
            if hasattr(job_application, key):
                setattr(job_application, key, value)
        db.session.commit()

    @staticmethod
    def delete_job_application(job_application_id):
        job_application = JobApplication.query.get(job_application_id)
        if not job_application:
            raise ValueError("Job application not found")
        db.session.delete(job_application)
        db.session.commit()