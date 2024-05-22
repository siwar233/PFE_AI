import os
from flask import Blueprint, request, jsonify, current_app, session
from werkzeug.utils import secure_filename
from datetime import datetime
from app import db
from models import Resume

upload_bp = Blueprint('upload_bp', __name__)

ALLOWED_EXTENSIONS = {'pdf', 'doc', 'docx'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload_bp.route('/upload_resume', methods=['POST'])
def upload_resume():
    # Ensure user is logged in and is an HR
    if 'user_id' not in session or session.get('role') != 'HR':
        return jsonify({"message": "Unauthorized"}), 401

    # Get the candidate ID and file from the request
    candidate_id = request.form.get('candidate_id')
    post_name = request.form.get('post_name')
    file = request.files.get('file')

    if not candidate_id or not post_name or not file:
        return jsonify({"message": "Candidate ID, Post Name, and File are required!"}), 400

    if not allowed_file(file.filename):
        return jsonify({"message": "File type not allowed!"}), 400

    filename = secure_filename(file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    
    # Create the upload folder if it does not exist
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)

    file_path = os.path.join(upload_folder, filename)
    file.save(file_path)

    # Add entry to the Resume model
    new_resume = Resume(
        candidate_id=candidate_id,
        post_name=post_name,
        file_path=file_path,
        uploaded_at=datetime.utcnow()
    )
    
    try:
        db.session.add(new_resume)
        db.session.commit()
        return jsonify({"message": "Resume uploaded successfully!"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Resume could not be uploaded!", "error": str(e)}), 500
