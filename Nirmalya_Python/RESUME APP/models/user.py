from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(200),nullable = False)
    personalDetails = db.relationship('PersonalDetails',backref='user')
    projects = db.relationship('Projects',backref='user')
    experiences = db.relationship('Experiences',backref='user')
    education=db.relationship('Education',backref='user')
    certificates=db.relationship('Certificates',backref='user')
    skills=db.relationship('Skills',backref='user')
