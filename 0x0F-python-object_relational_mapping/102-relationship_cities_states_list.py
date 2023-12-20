#!/usr/bin/python3
"""Lists all City objects and corresponding State objects from the database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    db_name = argv[3]

    """Connection to MySQL server"""
    ask = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name)
    engine = create_engine(ask)
    Base.metadata.create_all(engine)

    """ Create session"""
    Session = sessionmaker(bind=engine)
    session = Session()

    """Query to retrieve all City objects with associated State objects"""
    cities = session.query(City).order_by(City.id).all()

    """Display results"""
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
