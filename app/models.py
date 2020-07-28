from app import db

class Tweet(db.Model):
    __tablename__ = 'tweet'
    tID = db.Column(db.Integer, primary_key=True)
    given_text = db.Column(db.String, nullable=False)
    selected_text = db.Column(db.String)
    primary_sent = db.Column(db.Integer, nullable=False)
    secondary_sent = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Tweet {}>'.format(self.tID)
