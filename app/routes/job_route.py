from flask import Blueprint, request, jsonify
from app.services.job_service import  get_job_posting_by_id, get_job_posting_by_title, get_job_postings_by_date, update_job_posting, get_distinct_job_titles

job_bp = Blueprint('job', __name__)

@job_bp.route('/job_postings/<int:job_posting_id>', methods=['GET'])
def get_job_posting(job_posting_id):
    # Example route to fetch a specific job posting by ID
    job_posting = get_job_posting_by_id(job_posting_id)
    if job_posting:
        # Return job posting as JSON response
        return jsonify(job_posting)
    else:
        return jsonify({"error": "Job posting not found"}), 404

@job_bp.route('/job_postings/title/<string:job_title>', methods=['GET'])
def get_job_postings_by_title(job_title):
    # Example route to fetch job postings by title
    job_postings = get_job_posting_by_title(job_title)
    # Return job postings as JSON response
    return jsonify(job_postings)

@job_bp.route('/job_postings/date', methods=['GET'])
def get_job_postings_by_date():
    # Example route to fetch job postings by posted date
    posted_date = request.args.get('posted_date')
    job_postings = get_job_postings_by_date(posted_date)
    # Return job postings as JSON response
    return jsonify(job_postings)

@job_bp.route('/job_postings/update/<int:job_posting_id>', methods=['PUT'])
def update_job(job_posting_id):
    # Example route to update a job posting
    # You can pass parameters in the request body to update specific fields
    data = request.json
    try:
        update_job_posting(job_posting_id, **data)
        return jsonify({"message": "Job posting updated successfully"})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@job_bp.route('/job_titles', methods=['GET'])
def get_all_job_titles():
    # Example route to fetch distinct job titles
    job_titles = get_distinct_job_titles()
    # Return job titles as JSON response
    return jsonify(job_titles)

