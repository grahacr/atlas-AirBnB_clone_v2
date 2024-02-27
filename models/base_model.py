#!/usr/bin/python3

"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime as dt
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import models

base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, default=dt.utcnow(), nullable = False)
    updated_at = Column(DateTime, default=dt.utcnow(), nullable = False)

    def __init__(self, *args, **kwargs):
        class_name = kwargs.pop('__class__', None)
        for key, value in kwargs.items():
            setattr(self, key, value)
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = dt.now()
            self.updated_at = dt.now()
        else:
            self.updated_at = dt.strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = dt.strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = dt.now()
        storage.new(self) 
        storage.save()



    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = self.__dict__.copy()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        dictionary.update({'__class__':
                        (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        models.storage.delete(self)