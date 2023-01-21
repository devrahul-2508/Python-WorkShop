from config import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(200),nullable = False)
    personalDetails = db.relationship('Personal Details',backref='user')
    projects = db.relationship('Projects',backref='user')
