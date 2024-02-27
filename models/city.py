#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, base

class City(BaseModel, base): 
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    id = Column(String(60), primary_key=True, nullable=False) 
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", backref="city", cascade="all, delete")
