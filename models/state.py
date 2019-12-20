#!/usr/bin/python3
"""This is the state class"""
import os
from models.base_model import BaseModel
from models.city import City
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


Base = declarative_base()
HBNB_TYPE_STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if HBNB_TYPE_STORAGE == "db":
        cities = relationship(
            "City", cascade="all, delete",
            backref="state"
        )
    elif HBNB_TYPE_STORAGE == "file":
        ct = {}
        for k, v in models.storage.all(City).items():
            if v.state_id == State.id:
                ct[k] = v
        cities = ct
