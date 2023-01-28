from config import db

class Experiences(db.Model):
    __tablename__ = "experiences"
    id = db.Column(db.Integer,primary_key=True)
    company_name = db.Column(db.String(200),nullable = False)
    role=db.Column(db.String(200),nullable = False)
    role_desc=db.Column(db.String(200),nullable = False)
    start_date=db.Column(db.String(200),nullable = False)
    end_date=db.Column(db.String(200),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

