from flask import Flask,jsonify,request
from flask_cors import CORS
from os import environ
import os
from config import db,SECRET_KEY,load_dotenv
from models.user import User
from models.personalDetails import PersonalDetails
from models.projects import Projects
from models.education import Education
from models.experiences import Experiences
from models.certificates import Certificates
from models.skills import Skills

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('DB_URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        #db.drop_all()
        """
        Create an endpoint

        Use form data to take the responses from the user
        Use username for indexing a user
            - Sign up user
            - add personal details
            - add experience details
            - add project details
            - add education details
            - add certificate details
            - add skills details
        """
        @app.route("/sign_up", methods=['POST'])
        def sign_up():
            data = request.form.to_dict(flat=True)

            new_user = User(
                username = data["username"]
            )
            db.session.add(new_user)
            db.session.commit()

            return "User added successfulyy"

        @app.route("/add_personal_details", methods=['POST'])
        def add_personal_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()
            """
            {
                "name": "",
                "email": "",
                "phone": "",
                "address": "",
                "linkedin_link": ""
            }
            """
            personal_details = request.get_json()

            new_personal_details = PersonalDetails(
                name=personal_details["name"],
                email=personal_details["email"],
                phone=personal_details["phone"],
                address=personal_details["address"],
                linkedin_link=personal_details["linkedin_link"],
                user_id = user.id
            )

            db.session.add(new_personal_details)
            db.session.commit()
            return "Personal Details added successfully"

        @app.route("/add_experience_details",methods=["POST"])
        def add_experience_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            experience_details = request.get_json()

        @app.route("/add_projects_details",methods=['POST'])
        def add_project_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            project_details = request.get_json()


        @app.route("/add_education_details",methods=['POST'])
        def add_education_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            education_details = request.get_json()

        @app.route("/add_certificate_details",methods=['POST'])
        def add_certificate_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            certificate_details = request.get_json()

        @app.route("/add_skill_details",methods=['POST'])
        def add_skill_details():
            username = request.args.get('username')
            user = User.query.filter_by(username=username).first()

            skill_details = request.get_json()    





        db.create_all()
        db.session.commit()
        return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

