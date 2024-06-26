#!/usr/bin/python3

"""
Script that deletes all State objects with  name containing the letter a
from  database hbtn_0e_6_usa.
Parameters for script: mysql username, mysql password, database name.
Must use the `SQLAlchemy` module.
Must import `State` and `Base` from `model_state` -
`from model_state import Base, State`
Script should connect to  MySQL server runnimg on `localhost`  port `3306`
Code should not be executed when imported.
"""

from sys import argv
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # Check if the number of arguments is correct
    if len(argv) != 4:
        print("Usage: {} <username> <password> <database>".format(argv[0]))
        exit()

    # Creating the connection string (engine for database)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Creating an instance of Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying the State Object for states that contain the letter a
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')).all()

    # deleting the State Objects
    for state in states_to_delete:
        session.delete(state)

    # commit the changes
    session.commit()

    # Closing the session
    session.close()
