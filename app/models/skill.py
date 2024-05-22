from app import db
from sqlalchemy.exc import IntegrityError


class Skill(db.Model):
    __tablename__ = 'skills'
    skill_id = db.Column(db.Integer, primary_key=True)
    skill_name = db.Column(db.String(80), nullable=False, unique=True)
    candidate_skills = db.relationship('CandidateSkill', backref='skill', lazy=True)


    
    @staticmethod
    def add_skill(skill_name):
        new_skill = Skill(skill_name=skill_name)
        db.session.add(new_skill)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Skill with this name already exists")

    @staticmethod
    def get_skill_by_id(skill_id):
        return Skill.query.get(skill_id)

    @staticmethod
    def get_skill_by_name(skill_name):
        return Skill.query.filter_by(skill_name=skill_name).first()

    @staticmethod
    def update_skill(skill_id, skill_name):
        skill = Skill.query.get(skill_id)
        if not skill:
            raise ValueError("Skill not found")
        skill.skill_name = skill_name
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Skill with this name already exists")

    @staticmethod
    def delete_skill(skill_id):
        skill = Skill.query.get(skill_id)
        if not skill:
            raise ValueError("Skill not found")
        db.session.delete(skill)
        db.session.commit()
