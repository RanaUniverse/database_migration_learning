"""
For this repo this is the starting point
I will asume to start this python file which
will generate the database table if not exists
and then insert the data into it
"""

from sqlmodel import Session


from database_code.db_make import engine, create_db_and_tables
from database_code.models import HeroModel


def create_hero():
    hero_1 = HeroModel(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = HeroModel(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = HeroModel(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

    with Session(engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)

        session.commit()


if __name__=="__main__":
    create_db_and_tables()
    create_hero()