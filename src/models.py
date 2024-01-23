import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    username = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(40), nullable=False)
    favorites = Column(String(200), ForeignKey("favorites.favorites_url"))


class Favorites(Base):
    __tablename__ = "favorites"

    favorites_id = Column(Integer, primary_key=True)
    favorites_url = Column(String(200), nullable=False)


class Characters(Base):
    __tablename__ = "characters"

    character_id = Column(Integer, primary_key=True)
    character_name = Column(String(100), nullable=False)
    homeworld = Column(String(40), ForeignKey("planets.name"))
    film_appearences = Column(Integer, ForeignKey("film.film_id"))
    used_vehicles = Column(Integer, ForeignKey("vehicles.vehicle_id"))


class Films(Base):
    __tablename__ = "films"

    film_id = Column(Integer, primary_key=True)
    film_length = Column(Integer, nullable=False)
    film_title = Column(String(40), nullable=False)


class Planets(Base):
    __tablename__ = "planets"

    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(40), nullable=False)   


class Vehicles(Base):
    __tablename__ = "vehicles"

    vehicles_id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(40), nullable=False)


class Starships(Base):
    __tablename__ = "starships"

    starship_id = Column(Integer, primary_key=True)
    starship_name = Column(String(40), nullable=False)


    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')
