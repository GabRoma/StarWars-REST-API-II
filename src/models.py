from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#User start
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
        }
#User end

#Characters start
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    species = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)
    birthYear = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    mass = db.Column(db.String(250), nullable=False)
    hairColor = db.Column(db.String(250), nullable=False)
    eyeColor = db.Column(db.String(250), nullable=False)
    skinColor = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Characters %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "species": self.species,
            "gender": self.gender,
            "birthYear": self.birthYear,
            "height": self.height,
            "mass": self.mass,
            "hairColor": self.hairColor,
            "eyeColor": self.eyeColor,
            "skinColor": self.skinColor,
            "films": self.films,
            "created": self.created,
            "edited": self.edited
        }
#Characters end

#Planets start
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)
    surfaceWater = db.Column(db.String(250), nullable=False)
    rotationPeriod = db.Column(db.String(250), nullable=False)
    orbitalPeriod = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "diameter": self.diameter,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surfaceWater": self.surfaceWater,
            "rotationPeriod": self.rotationPeriod,
            "orbitalPeriod": self.orbitalPeriod,
            "gravity": self.gravity,
            "films": self.films,
            "created": self.created,
            "edited": self.edited,
        }
#Planets end

#Vehicles start
class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    url = db.Column(db.String(250), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), nullable=False)
    manufactured = db.Column(db.String(250), nullable=False)
    length = db.Column(db.String(250), nullable=False)
    consumables = db.Column(db.String(250), nullable=False)
    speed = db.Column(db.String(250), nullable=False)
    cost = db.Column(db.String(250), nullable=False)
    capacity = db.Column(db.String(250), nullable=False)
    crew = db.Column(db.String(250), nullable=False)
    passengers = db.Column(db.String(250), nullable=False)
    films = db.Column(db.String(250), nullable=False)
    created = db.Column(db.String(250), nullable=False)
    edited = db.Column(db.String(250), nullable=False)

    def __repr__(self):
        return '<Vehicles %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "type": self.type,
            "model": self.model,
            "manufactured": self.manufactured,
            "length": self.length,
            "consumables": self.consumables,
            "speed": self.speed,
            "cost": self.cost,
            "capacity": self.capacity,
            "crew": self.crew,
            "passengers": self.passengers,
            "films": self.films,
            "created": self.created,
            "edited": self.edited
        }
#Vehicles end

#Favorites start
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))
    # planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    # vehicles_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
            
    def __repr__(self):
        return '<Favorites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name
        }
#Favorites end