from app import db
from sqlalchemy.exc import IntegrityError


class Education(db.Model):
    __tablename__ = 'educations'
    education_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    degree = db.Column(db.String(80))
    institution_name = db.Column(db.String(80))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    field_of_study = db.Column(db.String(80))


    @staticmethod
    def add_education(candidate_id, degree=None, institution_name=None, start_date=None, end_date=None, field_of_study=None):

        new_education = Education(
            candidate_id=candidate_id,
            degree=degree,
            institution_name=institution_name,
            start_date=start_date,
            end_date=end_date,
            field_of_study=field_of_study
        )
        db.session.add(new_education)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the education record")

    @staticmethod
    def get_education_by_id(education_id):
        return Education.query.get(education_id)

    @staticmethod
    def get_educations_by_candidate_id(candidate_id):
        return Education.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_education(education_id, **kwargs):
        education = Education.query.get(education_id)
        if not education:
            raise ValueError("Education record not found")
        for key, value in kwargs.items():
            if hasattr(education, key):
                setattr(education, key, value)
        db.session.commit()

    @staticmethod
    def delete_education(education_id):
        education = Education.query.get(education_id)
        if not education:
            raise ValueError("Education record not found")
        db.session.delete(education)
        db.session.commit()