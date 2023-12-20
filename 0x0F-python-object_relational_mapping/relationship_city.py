#!/usr/bin/python3
"""Module that contains the City class"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    """Class representing the cities table"""
    __tablename__ = 'cities'
    id = Column(
            Integer,
            primary_key=True,
            nullable=False,
            autoincrement=True)

    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)
