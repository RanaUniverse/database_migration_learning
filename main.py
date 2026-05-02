"""
For this repo this is the starting point
I will asume to start this python file which
will generate the database table if not exists
and then insert the data into it
"""

from sqlmodel import Session


from database_code.db_make import engine
from database_code.models import HeroModel


import fake_data


def create_hero():

    hero_obj = HeroModel(
        name=fake_data.get_a_full_name(),
        secret_name=fake_data.one_word(),
        age=fake_data.age_int(),
    )

    with Session(engine) as session:
        session.add(hero_obj)
        session.commit()
        session.refresh(hero_obj)
        print(f"Hero has been inserted, {hero_obj}")


if __name__ == "__main__":
    # create_db_and_tables()
    how_many = 3
    for _ in range(how_many):
        create_hero()
