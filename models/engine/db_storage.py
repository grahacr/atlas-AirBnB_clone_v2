#!/usr/bin/python3
"""
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from sqlalchemy import create_engine, MetaData
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

Base = declarative_base()

class DBStorage:
    __engine: None
    __session: None
    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True)
        metadata = MetaData(self.__engine)
        if os.getenv('HBNB_ENV') == 'test':
            metadata.drop_all()

    def all(self, cls=None):
        results ={}
        if cls is None:
            for model in [User, State, City, Amenity, Place, Review]:
                objects = self.__session.query(model).all()
                for obj in objects:
                    key = f"{model.__tablename__}.{obj.id}"
                    results[key] = obj
        else:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = f"{cls.__tablename__}.{obj.id}"
                results[key] = obj
        return results

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        self.__sessionmaker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(self.__sessionmaker)
