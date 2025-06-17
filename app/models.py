from app import db

class Hero(db.model):
    __tabllename__ = 'heroes'
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(50), nullable=False)
    super_name = db.column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description

        }