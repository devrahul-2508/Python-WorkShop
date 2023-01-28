from config import db

class Certificates(db.Model):
    __tablename__ = 'certificates'
    id = db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable = False)
    start_date=db.Column(db.String(200),nullable = False)
    end_date=db.Column(db.String(200),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

