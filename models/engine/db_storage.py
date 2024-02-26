#!/usr/bin/python3
"""
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import (create_engine)
import os

Base = declarative_base()

class DBStorage:
    __engine: None
    __session: None
    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(f"mysql+mysqldb://{user}:{password}@{host}:{db}", pool_pre_pring=True)
        metadata = MetaData(engine)
        if os.getenv('HBNB_ENV') == 'test':
            metadata.drop_all()

    def all(self, cls=None):
