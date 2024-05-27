from app import db
from datetime import datetime
from sqlalchemy.exc import IntegrityError


class Job(db.Model):
    __tablename__ = 'jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    hr_id = db.Column(db.Integer, db.ForeignKey('hr.hr_id'), nullable=False)
    job_title = db.Column(db.String(120), nullable=False)
    job_description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text, nullable=False)
    location = db.Column(db.String(200))
    salary_range = db.Column(db.String(100))
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    closing_date = db.Column(db.DateTime)
    job_applications = db.relationship('JobApplication', backref='job', lazy=True)



    @staticmethod
    def add_job(hr_id, job_title, job_description, requirements, location=None, salary_range=None, closing_date=None):
        new_job = Job(
            hr_id=hr_id,
            job_title=job_title,
            job_description=job_description,
            requirements=requirements,
            location=location,
            salary_range=salary_range,
            closing_date=closing_date
        )
        db.session.add(new_job)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the job")

    @staticmethod
    def get_job_by_id(job_id):
        return Job.query.get(job_id)

    @staticmethod
    def update_job(job_id, **kwargs):
        job = Job.query.get(job_id)
        if not job:
            raise ValueError("Job not found")
        for key, value in kwargs.items():
            if hasattr(job, key):
                setattr(job, key, value)
        db.session.commit()

    @staticmethod
    def delete_job(job_id):
        job = Job.query.get(job_id)
        if not job:
            raise ValueError("Job not found")
        db.session.delete(job)
        db.session.commit()