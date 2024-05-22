#this part will conatin all the models that will impact to DB


# models/__init__.py

from app import db
from .user import User
from .candidate import Candidate
from .resume import Resume
from .experience import Experience
from .education import Education
from .skill import Skill
from .candidate_skill import CandidateSkill
from .certification import Certification
from .project import Project
from .language import Language
from .candidate_lang import CandidateLanguage
from .hr import HR
from .job import Job
from .job_app import JobApplication

# This part contains all the models that will impact the database
# Import all the models here to ensure they are registered with SQLAlchemy

__all__ = [
    'User', 
    'Candidate', 
    'Resume', 
    'Experience', 
    'Education', 
    'Skill', 
    'CandidateSkill', 
    'Certification', 
    'Project', 
    'Language', 
    'CandidateLanguage', 
    'HR', 
    'Job', 
    'JobApplication'
]

