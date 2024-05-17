from flask import Flask, render_template, request, redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sign_up import db, User
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError


app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pfe/2024@127.0.0.1/PFE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/sign_up', methods=['GET','POST'])
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

@app.route('/sign_in', methods=['POST'])
def sign_in():
    if request.method == 'POST':
        Username = request.form['Username']
        Password = request.form['Password']

        user = User.query.filter_by(Username=Username).first()
        if user and check_password_hash(user.password, Password):
            return render_template('index.html')
        else:
            error = 'Invalid username or password'
            return render_template('sign_in.html', error=error)
    
    return render_template('sign_in.html')

class HR_Accounts(db.Model):
    __tablename__ = 'HR_Accounts'
    Account_id = db.Column(db.BigInteger, primary_key=True)
    First_name = db.Column(db.String(255))
    Last_name = db.Column(db.String(255))
    Username = db.Column(db.String(255))
    Age = db.Column(db.Date)
    Phone = db.Column(db.String(255))
    Email = db.Column(db.String(255))
    Password = db.Column(db.String(255))


class JobPosting(db.Model):
    __tablename__ = 'job_posting'
    job_id = db.Column(db.BigInteger, primary_key=True)
    title = db.Column(db.String(255))
    uploaded_by = db.Column(db.BigInteger, db.ForeignKey('HR Accounts.account_id'))

def submit_post():
    if request.method == 'POST':
        post_name = request.form['postName']  # Get post name from the form
        uploaded_by = 1  # Assuming you have some logic to get the user's account ID
        new_job_post = JobPosting(title=post_name, uploaded_by=uploaded_by)
        try:
            db.session.add(new_job_post)
            db.session.commit()
            return redirect(url_for('home'))  # Redirect to homepage or wherever you want
        except IntegrityError:
            db.session.rollback()
            # Handle the case where the insertion failed
            return render_template('error.html', message="Error occurred while saving the job post.")
        finally:
            db.session.close()

@app.route('/')
def home():
    return render_template('sign_in.html')



if __name__ == '__main__':
    app.run(debug=True)
    