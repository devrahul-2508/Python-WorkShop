from config import db

class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    confidence_score=db.Column(db.String(200),nullable = False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
