# -*- coding: utf-8 -*-

# Set up database connection

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.engine.url import URL

from LegoScraper.settings import DATABASE

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(URL(**DATABASE))

DeclarativeBase = declarative_base()

def create_lego_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class Lego(DeclarativeBase):
    """sqlalchemy lego model"""
    __tablename__ = 'lego'

    id = Column(Integer, primary_key=True)
    Pieces = Column('Pieces',Integer, nullable=True)
    Minifigs = Column('Minifigs',Integer, nullable=True)
    Notes = Column('Notes',String, nullable=True)
    Community = Column('Community',String, nullable=True)
