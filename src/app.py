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
from models import db, User, Planets, Characters, Vehicles, Favorites

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

    return jsonify("New user added successfully"), 200

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

    return jsonify("User data updated"), 200

#DELETE User
@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    thatuser = User.query.get(user_id)
    if thatuser is None:
        raise APIException('User not found', status_code=404)
    db.session.delete(thatuser)
    db.session.commit()

    return jsonify("User deleted"), 200

#GET Users
@app.route('/user', methods=['GET'])
def handle_user():
    allusers = User.query.all()
    results = list(map(lambda item: item.serialize(),allusers))

    return jsonify(results), 200

#GET Single User
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
        name=request_body_character["name"], 
        url=request_body_character["url"], 
        species=request_body_character["species"],
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

    return jsonify("New character added successfully"), 200

#UPDATE Character
@app.route('/characters/<int:characters_id>', methods=['PUT'])
def update_character(characters_id):

    request_body_character = request.get_json()

    thisCharacter = Characters.query.get(characters_id)
    if thisCharacter is None:
        raise APIException('Character not found', status_code=404)
    if "name" in request_body_character:
        thisCharacter.name = body["name"]
    if "url" in request_body_character:
        thisCharacter.url = body["url"]
    if "species" in request_body_character:
        thisCharacter.species = request_body_character["species"]
    if "gender" in request_body_character:
        thisCharacter.gender = request_body_character["gender"]
    if "birthYear" in request_body_character:
        thisCharacter.birthYear = request_body_character["birthYear"]
    if "height" in request_body_character:
        thisCharacter.height = request_body_character["height"]
    if "mass" in request_body_character:
        thisCharacter.mass = request_body_character["mass"]
    if "hairColor" in request_body_character:
        thisCharacter.hairColor = request_body_character["hairColor"]
    if "eyeColor" in request_body_character:
        thisCharacter.eyeColor = request_body_character["eyeColor"]
    if "skinColor" in request_body_character:
        thisCharacter.skinColor = request_body_character["skinColor"]
    if "films" in request_body_character:
        thisCharacter.films = request_body_character["films"]
    if "created" in request_body_character:
        thisCharacter.created = request_body_character["created"]
    if "edited" in request_body_character:
        thisCharacter.edited = request_body_character["edited"]
    db.session.commit()

    return jsonify("Character updated"), 200

#DELETE Character
@app.route('/characters/<int:characters_id>', methods=['DELETE'])
def delete_character(characters_id):
    thatCharacter = Characters.query.get(characters_id)
    if thatCharacter is None:
        raise APIException('Character not found', status_code=404)
    db.session.delete(thatCharacter)
    db.session.commit()

    return jsonify("Character deleted"), 200

#GET Characters
@app.route('/characters', methods=['GET'])
def handle_characters():
    allcharacters = Characters.query.all()
    charactersList = list(map(lambda char: char.serialize(),allcharacters))

    return jsonify(charactersList), 200

#GET Single Character
@app.route('/characters/<int:characters_id>', methods=['GET'])
def single_character(characters_id):
    
    character = Characters.query.filter_by(id=characters_id).first()
    if character is None:
        raise APIException('Character not found', status_code=404)
    return jsonify(character.serialize()), 200

#Planets

#POST Planet
@app.route('/planets', methods=['POST'])
def create_planet():

    request_body_planet = request.get_json()

    newPlanet = Planets(
        name=request_body_planet["name"],
        url=request_body_planet["url"],
        diameter=request_body_planet["diameter"],
        population=request_body_planet["population"],
        climate=request_body_planet["climate"],
        terrain=request_body_planet["terrain"],
        surfaceWater=request_body_planet["surfaceWater"],
        rotationPeriod=request_body_planet["rotationPeriod"],
        orbitalPeriod=request_body_planet["orbitalPeriod"],
        gravity=request_body_planet["gravity"],
        films=request_body_planet["films"],
        created=request_body_planet["created"],
        edited=request_body_planet["edited"]
        )
    db.session.add(newPlanet)
    db.session.commit()

    return jsonify("New planet added successfully"), 200

#UPDATE Planet
@app.route('/planets/<int:planets_id>', methods=['PUT'])
def update_planet(planets_id):

    request_body_planet = request.get_json()

    thisPlanet = Planets.query.get(planets_id)
    if thisPlanet is None:
        raise APIException('Planet not found', status_code=404)
    if "name" in request_body_planet:
        thisPlanet.name = body["name"]
    if "url" in request_body_planet:
        thisPlanet.url = body["url"]
    if "diameter" in request_body_planet:
        thisPlanet.diameter = request_body_planet["diameter"]
    if "population" in request_body_planet:
        thisPlanet.population = request_body_planet["population"]
    if "climate" in request_body_planet:
        thisPlanet.climate = request_body_planet["climate"]
    if "terrain" in request_body_planet:
        thisPlanet.terrain = request_body_planet["terrain"]
    if "surfaceWater" in request_body_planet:
        thisPlanet.surfaceWater = request_body_planet["surfaceWater"]
    if "rotationPeriod" in request_body_planet:
        thisPlanet.rotationPeriod = request_body_planet["rotationPeriod"]
    if "orbitalPeriod" in request_body_planet:
        thisPlanet.orbitalPeriod = request_body_planet["orbitalPeriod"]
    if "gravity" in request_body_planet:
        thisPlanet.gravity = request_body_planet["gravity"]
    if "films" in request_body_planet:
        thisPlanet.films = request_body_planet["films"]
    if "created" in request_body_planet:
        thisPlanet.created = request_body_planet["created"]
    if "edited" in request_body_planet:
        thisPlanet.edited = request_body_planet["edited"]
    db.session.commit()

    return jsonify("Planet updated"), 200

#DELETE Planet
@app.route('/planets/<int:planets_id>', methods=['DELETE'])
def delete_planet(planets_id):
    thatPlanet = Planets.query.get(planets_id)
    if thatPlanet is None:
        raise APIException('Planet not found', status_code=404)
    db.session.delete(thatPlanet)
    db.session.commit()

    return jsonify("Planet deleted"), 200

#GET Planets
@app.route('/planets', methods=['GET'])
def handle_planets():
    allplanets = Planets.query.all()
    planetsList = list(map(lambda p: p.serialize(),allplanets))

    return jsonify(planetsList), 200

#GET Single Planet
@app.route('/planets/<int:planets_id>', methods=['GET'])
def single_planet(planets_id):
    
    planet = Planets.query.filter_by(id=planets_id).first()
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    return jsonify(planet.serialize()), 200

#Vehicles

#POST Vehicle
@app.route('/vehicles', methods=['POST'])
def create_vehicle():

    request_body_vehicle = request.get_json()

    newVehicle = Vehicles(
        name=request_body_vehicle["name"],
        url=request_body_vehicle["url"],
        type=request_body_vehicle["type"],
        model=request_body_vehicle["model"],
        manufactured=request_body_vehicle["manufactured"],
        length=request_body_vehicle["length"],
        consumables=request_body_vehicle["consumables"],
        speed=request_body_vehicle["speed"],
        cost=request_body_vehicle["cost"],
        capacity=request_body_vehicle["capacity"],
        crew=request_body_vehicle["crew"],
        passengers=request_body_vehicle["passengers"],
        films=request_body_vehicle["films"],
        created=request_body_vehicle["created"],
        edited=request_body_vehicle["edited"]
        )
    db.session.add(newVehicle)
    db.session.commit()

    return jsonify("New vehicle added successfully"), 200

#UPDATE Vehicle
@app.route('/vehicles/<int:vehicles_id>', methods=['PUT'])
def update_vehicle(vehicles_id):

    request_body_vehicle = request.get_json()

    thisVehicle = Vehicles.query.get(vehicles_id)
    if thisVehicle is None:
        raise APIException('Vehicle not found', status_code=404)
    if "name" in request_body_vehicle:
        thisVehicle.name = body["name"]
    if "url" in request_body_vehicle:
        thisVehicle.url = body["url"]
    if "type" in request_body_vehicle:
        thisVehicle.type = request_body_vehicle["type"]
    if "model" in request_body_vehicle:
        thisVehicle.model = request_body_vehicle["model"]
    if "manufactured" in request_body_vehicle:
        thisVehicle.manufactured = request_body_vehicle["manufactured"]
    if "length" in request_body_vehicle:
        thisVehicle.length = request_body_vehicle["length"]
    if "consumables" in request_body_vehicle:
        thisVehicle.consumables = request_body_vehicle["consumables"]
    if "speed" in request_body_vehicle:
        thisVehicle.speed = request_body_vehicle["speed"]
    if "cost" in request_body_vehicle:
        thisVehicle.cost = request_body_vehicle["cost"]
    if "capacity" in request_body_vehicle:
        thisVehicle.capacity = request_body_vehicle["capacity"]
    if "crew" in request_body_vehicle:
        thisVehicle.crew = request_body_vehicle["crew"]
    if "passengers" in request_body_vehicle:
        thisVehicle.passengers = request_body_vehicle["passengers"]
    if "films" in request_body_vehicle:
        thisVehicle.films = request_body_vehicle["films"]
    if "created" in request_body_vehicle:
        thisVehicle.created = request_body_vehicle["created"]
    if "edited" in request_body_vehicle:
        thisVehicle.edited = request_body_vehicle["edited"]
    db.session.commit()

    return jsonify("Vehicle updated"), 200

#DELETE Vehicle
@app.route('/vehicles/<int:vehicles_id>', methods=['DELETE'])
def delete_vehicle(vehicles_id):
    thatVehicle = Vehicles.query.get(vehicles_id)
    if thatVehicle is None:
        raise APIException('Vehicle not found', status_code=404)
    db.session.delete(thatVehicle)
    db.session.commit()

    return jsonify("Vehicle deleted"), 200

#GET Vehicles
@app.route('/vehicles', methods=['GET'])
def handle_vehicles():
    allvehicles = Vehicles.query.all()
    vehiclesList = list(map(lambda v: v.serialize(),allvehicles))

    return jsonify(vehiclesList), 200

#GET Single Vehicle
@app.route('/vehicles/<int:vehicles_id>', methods=['GET'])
def single_vehicle(vehicles_id):
    
    vehicle = Vehicles.query.filter_by(id=vehicles_id).first()
    if vehicle is None:
        raise APIException('Vehicle not found', status_code=404)
    return jsonify(vehicle.serialize()), 200

#Favorites

#POST Favorite Character
@app.route('/user/<int:user_id>/favorites/characters', methods=['POST'])
def add_favorite_character(user_id):
    request_body_favorite = request.get_json()
    newFav = Favorites(
        user_id=user_id, characters_id=request_body_favorite["characters_id"])
    db.session.add(newFav)
    db.session.commit()

    return jsonify("Character added to favorites"), 200

#DELETE Favorite Character
@app.route('/user/<int:user_id>/favorites/characters/', methods=['DELETE'])
def delete_favorite_character(user_id):
    request_body = request.get_json()
    thatFav = Favorites.query.filter_by(user_id=user_id, characters_id=request_body["characters_id"]).first()
    if thatFav is None:
        raise APIException('Favorite not found', status_code=404)
    db.session.delete(thatFav)
    db.session.commit()

    return jsonify("Character deleted from favorites"), 200

#POST Favorite Planet
@app.route('/user/<int:user_id>/favorites/planets', methods=['POST'])
def add_favorite_planet(user_id):
    
    request_body_favorite = request.get_json()

    newFav = Favorites(
        user_id=user_id, planets_id=request_body_favorite["planets_id"])
    db.session.add(newFav)
    db.session.commit()

    return jsonify("Planet added to favorites"), 200

#DELETE Favorite Planet
@app.route('/user/<int:user_id>/favorites/planets/', methods=['DELETE'])
def delete_favorite_planet(user_id):
    request_body = request.get_json()
    thatFav = Favorites.query.filter_by(user_id=user_id, planets_id=request_body["planets_id"]).first()
    if thatFav is None:
        raise APIException('Favorite not found', status_code=404)
    db.session.delete(thatFav)
    db.session.commit()

    return jsonify("Planet deleted from favorites"), 200

#POST Favorite Vehicle
@app.route('/user/<int:user_id>/favorites/vehicles', methods=['POST'])
def add_favorite_vehicle(user_id):
    
    request_body_favorite = request.get_json()

    newFav = Favorites(
        user_id=user_id, vehicles_id=request_body_favorite["vehicles_id"])
    db.session.add(newFav)
    db.session.commit()

    return jsonify("Vehicle added to favorites"), 200

#DELETE Favorite Vehicle
@app.route('/user/<int:user_id>/favorites/vehicles/', methods=['DELETE'])
def delete_favorite_vehicle(user_id):
    request_body = request.get_json()
    thatFav = Favorites.query.filter_by(user_id=user_id, vehicles_id=request_body["vehicles_id"]).first()
    if thatFav is None:
        raise APIException('Favorite not found', status_code=404)
    db.session.delete(thatFav)
    db.session.commit()

    return jsonify("Vehicle deleted from favorites"), 200

#GET Favorites
@app.route('/user/<int:user_id>/favorites', methods=['GET'])
def handle_favorites(user_id):
    allfavorites = Favorites.query.filter_by(user_id=user_id).all()
    favoritesList = list(map(lambda fav: fav.serialize(),allfavorites))

    return jsonify(favoritesList), 200

# #GET Single Favorite 
@app.route('/user/<int:user_id>/favorites/<int:favorites_id>', methods=['GET'])
def single_fav(user_id, favorites_id):

    favorite = Favorites.query.filter_by(user_id=user_id, id=favorites_id).first()
    if favorite is None:
        raise APIException('Favorite not found', status_code=404)
    return jsonify(favorite.serialize()), 200

#Endpoints end

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
