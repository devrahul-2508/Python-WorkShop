from flask import Flask,jsonify,request
from flask_cors import CORS
from os import environ
from config import db,SECRET_KEY
from dotenv import load_dotenv
from models.user import User
from models.personalDetails import PersonalDetails
from models.projects import Projects

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_ECHO"] = False
    app.secret_key = SECRET_KEY
    db.init_app(app)
    print("DB Initialized Successfully")

    with app.app_context():
        db.create_all()
        db.session.commit()
        return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

