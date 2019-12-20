#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import place_amenity

Base = declarative_base()


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
