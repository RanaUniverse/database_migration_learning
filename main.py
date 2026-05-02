"""
For this repo this is the starting point
I will asume to start this python file which
will generate the database table if not exists
and then insert the data into it
"""

from sqlmodel import Session


from database_code.db_make import (
    engine,
    # create_db_and_tables,
)

# from database_code.hero_model import HeroModel
# from database_code.team_model import TeamModel

from database_code import (
    HeroModel,
    TeamModel,
)


import fake_data


def create_hero():

    hero_obj = HeroModel(
        name=fake_data.get_a_full_name(),
        secret_name=fake_data.one_word(),
        age=fake_data.age_int(),
        phone="1234566741",
    )

    with Session(engine) as session:
        session.add(hero_obj)
        session.commit()
        session.refresh(hero_obj)
        print(f"Hero has been inserted, {hero_obj}")


def create_hero_and_team():
    with Session(engine) as session:
        team_obj = TeamModel(
            name=fake_data.get_a_full_name(),
            headquarters=fake_data.one_word(),
        )
        hero_obj = HeroModel(
            name=fake_data.get_a_full_name(),
            secret_name=fake_data.one_word(),
            age=fake_data.age_int(),
            phone="1234566741",
        )
        hero_obj.team = team_obj
        session.add(hero_obj)
        session.commit()
        session.refresh(hero_obj)
        print("Hero details are", hero_obj)


if __name__ == "__main__":
    # create_db_and_tables()
    how_many = 3
    for _ in range(how_many):
        # create_hero()
        create_hero_and_team()
