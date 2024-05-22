from app import db
from sqlalchemy.exc import IntegrityError


class Certification(db.Model):
    __tablename__ = 'certifications'
    certification_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    certification_name = db.Column(db.String(120), nullable=False)
    issuing_organization = db.Column(db.String(120))
    issue_date = db.Column(db.Date)
    expiration_date = db.Column(db.Date)


    @staticmethod
    def add_certification(candidate_id, certification_name, issuing_organization=None, issue_date=None, expiration_date=None):
        new_certification = Certification(
            candidate_id=candidate_id,
            certification_name=certification_name,
            issuing_organization=issuing_organization,
            issue_date=issue_date,
            expiration_date=expiration_date
        )
        db.session.add(new_certification)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the certification")

    @staticmethod
    def get_certification_by_id(certification_id):
        return Certification.query.get(certification_id)

    @staticmethod
    def get_certifications_by_candidate_id(candidate_id):
        return Certification.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_certification(certification_id, **kwargs):
        certification = Certification.query.get(certification_id)
        if not certification:
            raise ValueError("Certification not found")
        for key, value in kwargs.items():
            if hasattr(certification, key):
                setattr(certification, key, value)
        db.session.commit()

    @staticmethod
    def delete_certification(certification_id):
        certification = Certification.query.get(certification_id)
        if not certification:
            raise ValueError("Certification not found")
        db.session.delete(certification)
        db.session.commit()