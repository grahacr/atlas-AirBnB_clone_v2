#!/usr/bin/python3
""" holds class State"""
from models.base_model import BaseModel, base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, base):
    """Representation of state """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            import models
            city_objs = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_objs.append(city)
                    return city_objs
