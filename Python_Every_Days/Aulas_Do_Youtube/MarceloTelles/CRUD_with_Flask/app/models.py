from app import db

class Item(db.model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), mullable=False)
    description = db.Collumn(db.String(200), mullable=True)