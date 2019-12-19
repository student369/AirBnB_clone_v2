#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship(
        "Place", cascade="all, delete",
        backref="user"
    )
    reviews = relationship(
        "Review", cascade="all, delete",
        backref="user"
    )
