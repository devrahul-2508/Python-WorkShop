from config import db

class PersonalDetails(db.Model):
    __tablename__ = 'personalDetails'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    phone = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    linkedin_link = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))