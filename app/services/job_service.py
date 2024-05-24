# hr_service.py

from datetime import datetime
from app import db
from models import JobPosting, Candidate, Interview

def create_job_posting(job_title, job_description, requirements, location, salary_range):
    new_job_posting = JobPosting(
        title=job_title,
        description=job_description,
        requirements=requirements,
        location=location,
        salary_range=salary_range,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow()
    )

    try:
        db.session.add(new_job_posting)
        db.session.commit()
        return {"message": "Job posting created successfully!"}
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Error creating job posting: {e}")

def get_job_posting_by_id(job_posting_id):
    return JobPosting.query.get(job_posting_id)

