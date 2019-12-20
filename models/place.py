#!/usr/bin/python3
"""This is the place class"""
import os
import models
from models.base_model import BaseModel
from models import Place, Amenity, Review
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship

Base = declarative_base()
HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")

place_amenity = Table(
    "place_amenity", Base.metadata,
    Column(
        "place_id", String(60),
        ForeignKey("Place.id"), nullable=False,
        primary_key=True
    ),
    Column(
        "amenity_id", String(60),
        ForeignKey("Amenity.id"), nullable=False,
        primary_key=True
    )
)


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
        amenities = relationship(
            "Amenity", secondary=place_amenity,
            view_only=False
        )
    elif HBNB_TYPE_STORAGE == "file":

        @property
        def reviews(self):
            """Review:list Returns a list of Reviews"""
            lst = []
            for k, v in models.storage.all(Review).items():
                if v.place_id == Place.id:
                    lst.append(v)
            return (lst)

        @property
        def amenities(self):
            """Amenity:dict Returns the amenities"""
            lst = []
            for k, v in models.storage.all(Amenity).items():
                if v.id in self.amenity_ids:
                    lst.append(v)
            return (lst)

        @amenities.setter
        def amenities(self, value):
            if isinstance(value, Amenity):
                self.amenity_ids.append(value.id)
