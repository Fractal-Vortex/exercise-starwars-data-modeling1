from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    

    favorites = relationship("Favorites", back_populates="user")



class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    specie = Column(String(100))
    affiliation = Column(String(100))

    favorite = relationship("Favorites", back_populates="character")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))

    favorites = relationship("Favorites", back_populates="planet")


class Ships(Base):
    __tablename__ = 'ships'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    model = Column(String(100))
    manufacturer = Column(String(100))

    favorites = relationship("Favorites", back_populates="ship")



class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    character_id = Column(Integer, ForeignKey("characters.id"), nullable=True)
    planet_id = Column(Integer, ForeignKey("planets.id"), nullable=True)
    ship_id = Column(Integer, ForeignKey("ships.id"), nullable=True)



    user = relationship("User", back_populates="favorites")
    character = relationship("Characters", back_populates="favorites")
    planet = relationship("Planets", back_populates="favorites")
    ship = relationship("Ships", back_populates="favorites")



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
