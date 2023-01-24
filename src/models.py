import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table person 
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hairColor = Column(String(250), nullable=False)


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person 
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Population = Column(String(250), nullable=False)
    Terrain = Column(String(250), nullable=False)
    
class Vehiculos (Base):
    __tablename__ = 'vehiculos'
    # Here we define columns for the table person 
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    





class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    planets_id = Column(Integer, ForeignKey('planets.id'))
    characters_id = Column(Integer, ForeignKey('characters.id'))
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'))

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
