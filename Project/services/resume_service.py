import os
from werkzeug.utils import secure_filename
from models import db, Resume
from flask import current_app
from datetime import datetime

class ResumeService:
    @staticmethod
    def save_resume(file, post_name, user_id):
        if file and ResumeService.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_folder = current_app.config['UPLOAD_FOLDER']
            file_path = os.path.join(upload_folder, filename)
            
            file.save(file_path)

            new_resume = Resume(
                filename=filename,
                file_path=file_path,
                post_name=post_name,
                user_id=user_id,
                uploaded_at=datetime.utcnow()
            )
            db.session.add(new_resume)
            db.session.commit()
            return new_resume
        else:
            raise ValueError("Invalid file type")

    @staticmethod
    def allowed_file(filename):
        allowed_extensions = {'pdf', 'doc', 'docx'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    @staticmethod
    def get_resume_by_id(resume_id):
        return Resume.query.get(resume_id)

    @staticmethod
    def get_all_resumes():
        return Resume.query.all()

    @staticmethod
    def delete_resume(resume_id):
        resume = Resume.query.get(resume_id)
        if not resume:
            raise ValueError("Resume not found")
        os.remove(resume.file_path)
        db.session.delete(resume)
        db.session.commit()
