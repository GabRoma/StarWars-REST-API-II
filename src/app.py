"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Planets, Characters, Vehicles

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)


#Endpoints start

#User

#POST User
@app.route('/user', methods=['POST'])
def create_user():

    request_body_user = request.get_json()

    newUser = User(username=request_body_user["username"], email=request_body_user["email"], password=request_body_user["password"])
    db.session.add(newUser)
    db.session.commit()

    return jsonify(request_body_user), 200

#UPDATE User
@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    request_body_user = request.get_json()

    thisuser = User.query.get(user_id)
    if thisuser is None:
        raise APIException('User not found', status_code=404)
    if "username" in request_body_user:
        thisuser.username = body["username"]
    if "email" in request_body_user:
        thisuser.email = body["email"]
    if "password" in request_body_user:
        thisuser.password = request_body_user["password"]
    db.session.commit()

    return jsonify(request_body_user), 200

#DELETE User
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    thatuser = User.query.get(user_id)
    if thatuser is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(thatuser)
    db.session.commit()

    return jsonify("user deleted"), 200

#GET Users
@app.route('/user', methods=['GET'])
def handle_user():
    allusers = User.query.all()
    results = list(map(lambda item: item.serialize(),allusers))

    return jsonify(results), 200

#GET single user
@app.route('/user/<int:user_id>', methods=['GET'])
def single_user(user_id):
    
    user = User.query.filter_by(id=user_id).first()
    return jsonify(user.serialize()), 200


#Characters

#POST Character
@app.route('/characters', methods=['POST'])
def create_character():

    request_body_character = request.get_json()

    newCharacter = Characters(
        name=request_body_character["name"], url=request_body_character["url"], species=request_body_character["species"],
        gender=request_body_character["gender"],
        birthYear=request_body_character["birthYear"],
        height=request_body_character["height"],
        mass=request_body_character["mass"],
        hairColor=request_body_character["hairColor"],
        eyeColor=request_body_character["eyeColor"],
        skinColor=request_body_character["skinColor"],
        films=request_body_character["films"],
        created=request_body_character["created"],
        edited=request_body_character["edited"])
    db.session.add(newCharacter)
    db.session.commit()

    return jsonify(request_body_character), 200

#GET Characters
@app.route('/characters', methods=['GET'])
def handle_characters():
    allcharacters = Characters.query.all()
    charactersList = list(map(lambda char: char.serialize(),allcharacters))

    return jsonify(charactersList), 200

#Single character
@app.route('/characters/<int:characters_name>', methods=['GET'])
def single_character(characters_name):
    
    character = Characters.query.filter_by(name=characters_name).first()
    return jsonify(character.serialize()), 200

#Planets
@app.route('/planets', methods=['GET'])
def handle_planets():
    allplanets = Planet.query.all()
    planetsList = list(map(lambda p: p.serialize(),allplanets))

    return jsonify(planetsList), 200

#Single planet
@app.route('/planets/<int:planets_name>', methods=['GET'])
def single_planet(planets_name):
    
    planet = Planets.query.filter_by(name=planets_name).first()
    return jsonify(planet.serialize()), 200

#Vehicles
@app.route('/vehicles', methods=['GET'])
def handle_vehicles():
    allvehicles = Vehicles.query.all()
    vehiclesList = list(map(lambda v: v.serialize(),allvehicles))

    return jsonify(vehiclesList), 200

#Single vehicle
@app.route('/vehicles/<int:vehicles_name>', methods=['GET'])
def single_vehicle(vehicles_name):
    
    vehicle = Vehicles.query.filter_by(name=vehicles_name).first()
    return jsonify(vehicle.serialize()), 200

#Favorites
@app.route('/favorites', methods=['GET'])
def handle_favorites():
    allfavorites = Favorites.query.all()
    favoritesList = list(map(lambda fav: fav.serialize(),allfavorites))

    return jsonify(favoritesList), 200

#Single favorite
@app.route('/favorites/<int:favorites_id>', methods=['GET'])
def single_favorite(favorites_id):
    
    favorite = Favorites.query.filter_by(id=favorites_id).first()
    return jsonify(favorite.serialize()), 200

#Endpoints end

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
