from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models import db, User, HR_Accounts, JobPosting
from ocr_utils import extract_text_from_pdf_file, create_connection, insert_experience, extract_experience_details
import os
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pfe/2024@127.0.0.1/PFE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

UPLOAD_FOLDER = 'uploads'

# Define Blueprint
bp = Blueprint('main', __name__)

@bp.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        First_name = request.form['First_name']
        Last_name = request.form['Last_name']
        Username = request.form['Username']
        Age = request.form['Age']
        Phone = request.form['Phone']
        Email = request.form['Email']
        Password = request.form['Password']

        new_user = User.user_signup(First_name, Last_name, Username, Age, Phone, Email, Password)

        return render_template('sign_in.html')

    return render_template('sign_up.html')



@bp.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        Username = request.form['Username']
        Password = request.form['Password']

        user = User.query.filter_by(Username=Username).first()
        if user and check_password_hash(user.Password, Password):
            return render_template('index.html')
        else:
            error = 'Invalid username or password'
            return render_template('sign_in.html', error=error)

    return render_template('sign_in.html')



@bp.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'pdf_file' not in request.files:
            return 'No file part'
        pdf_file = request.files['pdf_file']
        if pdf_file.filename == '':
            return 'No selected file'
        if pdf_file:
            filename = pdf_file.filename
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            pdf_file.save(filepath)
            text = extract_text_from_pdf_file(filepath)
            title, start_date, end_date, company = extract_experience_details(text)
            if title and start_date and end_date and company:
                conn, cursor = create_connection()
                insert_experience(cursor, title, start_date, end_date, company)
                conn.commit()
                cursor.close()
                conn.close()
                os.remove(filepath)
                return 'PDF uploaded, experience details extracted, and stored in the database successfully!'

    return 'No PDF uploaded'



@bp.route('/')
def home():
    return render_template('sign_in.html')

@bp.route('/submit_post', methods=['POST'])
def submit_post():
    if request.method == 'POST':
        post_name = request.form['postName']
        uploaded_by = 1  # Assuming you have some logic to get the user's account ID
        new_job_post = JobPosting(title=post_name, uploaded_by=uploaded_by)
        try:
            db.session.add(new_job_post)
            db.session.commit()
            return redirect(url_for('main.home'))
        except IntegrityError:
            db.session.rollback()
            return render_template('error.html', message="Error occurred while saving the job post.")
        finally:
            db.session.close()

# Register Blueprint
app.register_blueprint(bp)



if __name__ == '__main__':
    app.run(debug=True)
