from flask import request, jsonify
from app import app, db
from app.models import Hero, Power, HeroPower

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
    } for hero in heroes])

@app.route ('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify(hero.to_dict()), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all ()
    return jsonify([power.to_dict() for power in powers]), 200

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify(power.to_dict()), 200

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.get.query(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    data = request.get_json()
    power.description = data.get('description')

    errors = power.validate()
    if errors:
        return jsonify({"errors": errors}), 400
    db.session.commit()
    return jsonify(power.to_dict()), 200

@app.route('/heroe_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"}), 404
    hero_power = HeroPower(strength=strength, hero_id=hero_id, power_id=power_id)

    errors = hero_power.validate()
    if errors:
        return jsonify({"errors": errors}), 400
    
    db.session.add(hero_power)
    db.session.commit()
    return jsonify(hero_power.to_dict()), 201

