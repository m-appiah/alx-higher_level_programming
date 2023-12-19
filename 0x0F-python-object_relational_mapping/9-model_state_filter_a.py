#!/usr/bin/python3
"""Lists all State objects containing the letter 'a' from the database"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

    states_with_a = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))
