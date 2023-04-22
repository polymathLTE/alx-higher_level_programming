#!/usr/bin/python3
"""
this script prints all City objects from the database hbtn_0e_14_usa
"""
from model_city import Base, State, City
from sqlalchemy import (create_engine)
from sqlalchemy import join
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine(f"mysql+mysqldb://{sys.argv[2]}:\
    {sys.argv[1]}@localhost:3306/{sys.argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(City, State)\
                           .join(State, City.state_id == State.id):
        print(f"{instance.State.name}:\
        ({instance.City.id}) {instance.City.name}")
