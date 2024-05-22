from app import db
from sqlalchemy.exc import IntegrityError

class CandidateSkill(db.Model):
    __tablename__ = 'candidate_skills'
    candidate_skill_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    skill_id = db.Column(db.Integer, db.ForeignKey('skills.skill_id'), nullable=False)



    @staticmethod
    def add_candidate_skill(candidate_id, skill_id):
        new_candidate_skill = CandidateSkill(
            candidate_id=candidate_id,
            skill_id=skill_id
        )
        db.session.add(new_candidate_skill)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the candidate skill")

    @staticmethod
    def get_candidate_skill_by_id(candidate_skill_id):
        return CandidateSkill.query.get(candidate_skill_id)

    @staticmethod
    def get_skills_by_candidate_id(candidate_id):
        return CandidateSkill.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_candidate_skill(candidate_skill_id, **kwargs):
        candidate_skill = CandidateSkill.query.get(candidate_skill_id)
        if not candidate_skill:
            raise ValueError("Candidate skill not found")
        for key, value in kwargs.items():
            if hasattr(candidate_skill, key):
                setattr(candidate_skill, key, value)
        db.session.commit()

    @staticmethod
    def delete_candidate_skill(candidate_skill_id):
        candidate_skill = CandidateSkill.query.get(candidate_skill_id)
        if not candidate_skill:
            raise ValueError("Candidate skill not found")
        db.session.delete(candidate_skill)
        db.session.commit()