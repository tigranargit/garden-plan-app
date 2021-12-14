from application import db

class Beds(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    aspect = db.Column(db.String(50), nullable=False)
    plants = db.relationship('Plants', backref='bedbr')

class Plants(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable=False)
    plantbed = db.Column(db.String(50), nullable = False)
    bed_id = db.Column(db.Integer, db.ForeignKey('beds.id'), nullable=False)

