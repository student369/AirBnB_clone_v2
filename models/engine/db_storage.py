#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
import os
import inspect as ins
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

Base = declarative_base()
HBNB_MYSQL_USER = os.getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = os.getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = "localhost"
HBNB_MYSQL_DB = os.getenv("HBNB_MYSQL_DB")
HBNB_ENV = os.getenv("HBNB_ENV")


class DBStorage:
    """This class allow the connection to a MySQL
    database to do DB operations.
    Attributes:
        __engine: The engine to use
        __objects: The specific session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Create a new db_storage instance
        """
        self.__engine = create_engine(
            "mysql+mysqldb://{:s}:{:s}@{:s}:{:s}/{:s}"
            .format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
                HBNB_MYSQL_HOST, "3306", HBNB_MYSQL_DB
            ),
            pool_pre_ping=True
        )

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        else:
            Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        filt = {}
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if cls is not None and ins.isclass(cls):
            clsn = cls.__module__.split(".")[1]
            if clsn in HBNBCommand.all_classes:
                res = self.__session.query(cls).all()
                for o in res:
                    key = "{}.{}".format(
                        clsn, o.id
                    )
                    filt[key] = o
                self.__session.close()
                return filt
        for c in HBNBCommand.all_classes:
            res = self.__session.query(eval(c)).all()
            for o in res:
                key = "{}.{}".format(
                    c, o.id
                )
                filt[key] = o
        self.__session.close()
        return filt

    def new(self, obj):
        """Add an object to the current session
        Args:
            obj: given object
        """
        if obj:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            clsn = type(obj).__name__
            if clsn in HBNBCommand.all_classes:
                self.__session.add(obj)
                self.__session.commit()
                self.__session.close()

    def save(self):
        """serialize the file path to JSON file path
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete and object
        """
        if obj is not None:
            Session = sessionmaker(bind=self.__engine)
            self.__session = Session()
            clsn = type(obj).__name__
            if clsn in HBNBCommand.all_classes:
                self.__session.delete(obj)
                self.__session.commit()
                self.__session.close()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        self.__session = scoped_session(Session)
