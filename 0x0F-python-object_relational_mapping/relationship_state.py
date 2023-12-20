#!/usr/bin/python3
"""Module that contains the State class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing the states table"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True)

    name = Column(
            String(128),
            nullable=False)
    cities = relationship("City", cascade="all,delete", backref="state")
