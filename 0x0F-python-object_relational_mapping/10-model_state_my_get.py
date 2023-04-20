#!/usr/bin/python3
"""
script that lists all State objects
from the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # dialect+driver://username:password@host:port/database
    engine = create_engine(f"mysql+mysqldb://{sys.argv[2]}:{sys.argv[1]}@localhost:3306/{sys.argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).filter(State.name == sys.argv[4]):
        if len(instance) == 0:
            print("Not found")
        else:
            print(instance.id)
