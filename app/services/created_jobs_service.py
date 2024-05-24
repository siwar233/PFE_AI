from models import JobPosting, CandidateJobApplication

def get_all_jobs():
    return JobPosting.query.all()

def get_job_by_id(job_id):
    return JobPosting.query.get(job_id)

    '''
    def get_jobs_by_candidate_id(candidate_id):
    # First, get all the job applications made by the candidate
    job_applications = CandidateJobApplication.query.filter_by(candidate_id=candidate_id).all()
    
    # Extract the job IDs from the job applications
    job_ids = [job_app.job_id for job_app in job_applications]
    
    # Retrieve the job postings using the job IDs
    jobs = JobPosting.query.filter(JobPosting.id.in_(job_ids)).all()
    
    return jobs
'''