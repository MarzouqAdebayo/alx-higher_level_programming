#!/usr/bin/python3
"""
  a script that prints the first State object from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import Base, State
    from sqlalchemy import create_engine
    import sys
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = sessionmaker(bind=engine)()

    state = session.query(State).order_by(State.id).first()
    print("{}: {}".format(state.id, state.name))
