#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from models import Place
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

Base = declarative_base()
HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = "places"
    city_id = Column(
        String(60), ForeignKey("cities.id"), nullable=False
    )
    user_id = Column(
        String(60), ForeignKey("users.id"), nullable=False
    )
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(
        Integer, nullable=False,
        default=0
    )
    number_bathrooms = Column(
        Integer, nullable=False,
        default=0
    )
    max_guest = Column(
        Integer, nullable=False,
        default=0
    )
    price_by_night = Column(
        Integer, nullable=False,
        default=0
    )
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    amenity_ids = []
    if HBNB_TYPE_STORAGE == "db":
        reviews = relationship(
            "Review", cascade="all, delete",
            backref="place"
        )
    elif HBNB_TYPE_STORAGE == "file":
        ct = {}
        for k, v in models.storage.all(Review).items():            
            if v.place_id == Place.id:
                ct[k] = v
        reviews = ct
