from app import db
from sqlalchemy.exc import IntegrityError


class Language(db.Model):
    __tablename__ = 'languages'
    language_id = db.Column(db.Integer, primary_key=True)
    language_name = db.Column(db.String(80), nullable=False, unique=True)
    candidate_languages = db.relationship('CandidateLanguage', backref='language', lazy=True)


    @staticmethod
    def add_language(language_name):
        new_language = Language(language_name=language_name)
        db.session.add(new_language)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Language with this name already exists")

    @staticmethod
    def get_language_by_id(language_id):
        return Language.query.get(language_id)

    @staticmethod
    def get_language_by_name(language_name):
        return Language.query.filter_by(language_name=language_name).first()

    @staticmethod
    def update_language(language_id, language_name):
        language = Language.query.get(language_id)
        if not language:
            raise ValueError("Language not found")
        language.language_name = language_name
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Language with this name already exists")

    @staticmethod
    def delete_language(language_id):
        language = Language.query.get(language_id)
        if not language:
            raise ValueError("Language not found")
        db.session.delete(language)
        db.session.commit()
