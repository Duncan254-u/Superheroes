from app import db

# ----------------------------
# Hero Model
# ----------------------------
class Hero(db.Model):
    __tablename__ = 'heroes'  # ✅ Fix typo: '__tabllename__' → '__tablename__'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    super_name = db.Column(db.String)
    description = db.Column(db.String) 
    
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name,
            "description": self.description
        }

    def validate(self):
        errors = []
        if not self.description or len(self.description) < 20:
            errors.append("Description must be at least 20 characters long.")
        return errors


class Power(db.Model):
    __tablename__ = 'powers'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String)

    hero_powers = db.relationship('HeroPower', back_populates='power')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(50), nullable=False)
    
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "hero_id": self.hero_id,
            "power_id": self.power_id,
            "hero": {
                "id": self.hero.id,
                "super_name": self.hero.super_name
            },
            "power": self.power.to_dict()
        }

    def validate(self):
        if self.strength not in ['strong', 'weak', 'average']: 
            return ["Strength must be one of: strong, weak, average."]
        return []
