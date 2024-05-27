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

def get_job_posting_by_title(job_title):
    return JobPosting.query.filter_by(title=job_title).all()

def get_job_postings_by_date(posted_date):
    return JobPosting.query.filter(JobPosting.created_at >= posted_date).all()

#update

def update_job_posting(job_posting_id, job_title=None, job_description=None, requirements=None, location=None, salary_range=None):
    job_posting = get_job_posting_by_id(job_posting_id)
    if not job_posting:
        return {"message": "Job posting not found"}

    if job_title:
        job_posting.title = job_title
    if job_description:
        job_posting.description = job_description
    if requirements:
        job_posting.requirements = requirements
    if location:
        job_posting.location = location
    if salary_range:
        job_posting.salary_range = salary_range
    job_posting.updated_at = datetime.utcnow()

    try:
        db.session.commit()
        return {"message": "Job posting updated successfully!"}
    except Exception as e:
        db.session.rollback()
        raise ValueError(f"Error updating job posting: {e}")
    
def get_distinct_job_titles():
    job_titles = JobPosting.query.with_entities(JobPosting.title).distinct().all()
    return [job[0] for job in job_titles]