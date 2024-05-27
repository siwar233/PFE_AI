from app import db
from sqlalchemy.exc import IntegrityError



class Project(db.Model):
    __tablename__ = 'projects'
    project_id = db.Column(db.Integer, primary_key=True)
    candidate_id = db.Column(db.Integer, db.ForeignKey('candidates.candidate_id'), nullable=False)
    project_title = db.Column(db.String(120), nullable=False)
    project_description = db.Column(db.Text)
    technologies_used = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)


    @staticmethod
    def add_project(candidate_id, project_title, project_description=None, technologies_used=None, start_date=None, end_date=None):
        new_project = Project(
            candidate_id=candidate_id,
            project_title=project_title,
            project_description=project_description,
            technologies_used=technologies_used,
            start_date=start_date,
            end_date=end_date
        )
        db.session.add(new_project)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise ValueError("Error adding the project")

    @staticmethod
    def get_project_by_id(project_id):
        return Project.query.get(project_id)

    @staticmethod
    def get_projects_by_candidate_id(candidate_id):
        return Project.query.filter_by(candidate_id=candidate_id).all()

    @staticmethod
    def update_project(project_id, **kwargs):
        project = Project.query.get(project_id)
        if not project:
            raise ValueError("Project not found")
        for key, value in kwargs.items():
            if hasattr(project, key):
                setattr(project, key, value)
        db.session.commit()

    @staticmethod
    def delete_project(project_id):
        project = Project.query.get(project_id)
        if not project:
            raise ValueError("Project not found")
        db.session.delete(project)
        db.session.commit()