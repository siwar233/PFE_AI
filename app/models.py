from datetime import datetime
from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    candidates = db.relationship('Candidate', backref='user', lazy=True)

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

class Resume(db.Model):
    __tablename__ = 'resumes'
    resume_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    resume_file = db.Column(db.String(200), nullable=False)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    parsed_date = db.Column(db.DateTime)

class Experience(db.Model):
    __tablename__ = 'experiences'
    experience_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    job_title = db.Column(db.String(80), nullable=False)
    company_name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    job_description = db.Column(db.Text)

class Education(db.Model):
    __tablename__ = 'educations'
    education_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    degree = db.Column(db.String(80))
    institution_name = db.Column(db.String(80))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    field_of_study = db.Column(db.String(80))

class Skill(db.Model):
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(80), nullable=False, unique=True)
    candidate_skills = db.relationship('CandidateSkill', backref='skill', lazy=True)

class CandidateSkill(db.Model):
    __tablename__ = 'candidate_skills'
    candidate_skill_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), nullable=False)

class Certification(db.Model):
    __tablename__ = 'certifications'
    certification_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    certification_name = db.Column(db.String(120), nullable=False)
    issuing_organization = db.Column(db.String(120))
    issue_date = db.Column(db.Date)
    expiration_date = db.Column(db.Date)

class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    project_title = db.Column(db.String(120), nullable=False)
    project_description = db.Column(db.Text)
    technologies_used = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

class Language(db.Model):
    __tablename__ = 'languages'
    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(80), nullable=False, unique=True)
    candidate_languages = db.relationship('CandidateLanguage', backref='language', lazy=True)

class CandidateLanguage(db.Model):
    __tablename__ = 'candidate_languages'
    candidate_language_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.language_id'), nullable=False)
    proficiency_level = db.Column(db.String(80))
class HR(db.Model):
    __tablename__ = 'hr'
    hr_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    jobs = db.relationship('Job', backref='hr', lazy=True)

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

class JobApplication(db.Model):
    __tablename__ = 'job_applications'
    job_application_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)
    application_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(50), nullable=False, default='Pending')