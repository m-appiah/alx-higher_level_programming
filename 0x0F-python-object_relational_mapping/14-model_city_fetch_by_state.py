#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    ask = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name)
    engine = create_engine(ask)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(
            City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
