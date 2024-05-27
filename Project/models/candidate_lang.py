from app import db
from sqlalchemy.exc import IntegrityError

class CandidateLanguage(db.Model):
    __tablename__ = 'candidate_languages'
    candidate_language_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey('languages.language_id'), nullable=False)
    proficiency_level = db.Column(db.String(80))


    @staticmethod
    def add_candidate_language(candidate_id, language_id, proficiency_level):
        new_candidate_language = CandidateLanguage(
            candidate_id=candidate_id,
            language_id=language_id,
            proficiency_level=proficiency_level
        )
        db.session.add(new_candidate_language)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the candidate language")

    @staticmethod
    def get_candidate_language_by_id(candidate_language_id):
        return CandidateLanguage.query.get(candidate_language_id)

    @staticmethod
    def get_languages_by_candidate_id(candidate_id):
        return CandidateLanguage.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_candidate_language(candidate_language_id, **kwargs):
        candidate_language = CandidateLanguage.query.get(candidate_language_id)
        if not candidate_language:
            raise ValueError("Candidate language not found")
        for key, value in kwargs.items():
            if hasattr(candidate_language, key):
                setattr(candidate_language, key, value)
        db.session.commit()

    @staticmethod
    def delete_candidate_language(candidate_language_id):
        candidate_language = CandidateLanguage.query.get(candidate_language_id)
        if not candidate_language:
            raise ValueError("Candidate language not found")
        db.session.delete(candidate_language)
        db.session.commit()