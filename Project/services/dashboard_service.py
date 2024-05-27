from models import Candidate, CandidateLanguage, Project, Experience, Certification, CandidateSkillSet, Education, Resumes, JobApplication, Job, SkillSet, Skill
from sqlalchemy import func

class DashboardService:
    @staticmethod
    def get_candidate_info(candidate_id):
        candidate = Candidate.query.get(candidate_id)
        return candidate.serialize()

    @staticmethod
    def get_candidate_skills(candidate_id):
        skills = CandidateSkillSet.query.filter_by(candidate_id=candidate_id).all()
        return [skill.serialize() for skill in skills]

    @staticmethod
    def get_candidate_projects(candidate_id):
        projects = Project.query.filter_by(candidate_id=candidate_id).all()
        return [project.serialize() for project in projects]

    @staticmethod
    def get_candidate_experiences(candidate_id):
        experiences = Experience.query.filter_by(candidate_id=candidate_id).all()
        return [experience.serialize() for experience in experiences]

    @staticmethod
    def get_candidate_certifications(candidate_id):
        certifications = Certification.query.filter_by(candidate_id=candidate_id).all()
        return [certification.serialize() for certification in certifications]

    @staticmethod
    def get_job_applications(candidate_id):
        job_applications = JobApplication.query.filter_by(candidate_id=candidate_id).all()
        return [job_application.serialize() for job_application in job_applications]

    @staticmethod
    def get_job_application_stats():
        total_applications = JobApplication.query.count()
        application_status_count = JobApplication.query.with_entities(JobApplication.status, func.count()).group_by(JobApplication.status).all()
        return {'total_applications': total_applications, 'application_status_count': application_status_count}
