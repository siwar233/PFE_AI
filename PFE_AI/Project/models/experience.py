from app import db
from sqlalchemy.exc import IntegrityError


class Experience(db.Model):
    __tablename__ = 'experiences'
    experience_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    job_title = db.Column(db.String(80), nullable=False)
    company_name = db.Column(db.String(80), nullable=False)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    job_description = db.Column(db.Text)


    @staticmethod
    def add_experience(candidate_id, job_title, company_name, start_date=None, end_date=None, job_description=None):
        new_experience = Experience(
            candidate_id=candidate_id,
            job_title=job_title,
            company_name=company_name,
            start_date=start_date,
            end_date=end_date,
            job_description=job_description
        )
        db.session.add(new_experience)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the experience")

    @staticmethod
    def get_experience_by_id(experience_id):
        return Experience.query.get(experience_id)

    @staticmethod
    def get_experiences_by_candidate_id(candidate_id):
        return Experience.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_experience(experience_id, **kwargs):
        experience = Experience.query.get(experience_id)
        if not experience:
            raise ValueError("Experience not found")
        for key, value in kwargs.items():
            if hasattr(experience, key):
                setattr(experience, key, value)
        db.session.commit()

    @staticmethod
    def delete_experience(experience_id):
        experience = Experience.query.get(experience_id)
        if not experience:
            raise ValueError("Experience not found")
        db.session.delete(experience)
        db.session.commit()