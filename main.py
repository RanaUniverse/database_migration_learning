"""
For this repo this is the starting point
I will asume to start this python file which
will generate the database table if not exists
and then insert the data into it
"""

from sqlmodel import Session, select


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
        hero_obj_1 = HeroModel(
            name=fake_data.get_a_full_name(),
            secret_name=fake_data.one_word(),
            age=fake_data.age_int(),
            phone="111111111",
        )
        hero_obj_2 = HeroModel(
            name=fake_data.get_a_full_name(),
            secret_name=fake_data.one_word(),
            age=fake_data.age_int(),
            phone="222222222",
        )
        team_obj.heroes.append(hero_obj_1)
        team_obj.heroes.append(hero_obj_2)
        session.add(team_obj)
        session.commit()
        session.refresh(team_obj)
        print("Hero details are", team_obj.heroes)


def delete_a_hero_obj(hero_id: int):
    """
    i will pass the hero id as int and it will try to delte this form teh database
    """
    with Session(engine) as session:
        statement = select(HeroModel).where(HeroModel.id_ == hero_id)
        results = session.exec(statement)
        hero = results.one()
        session.delete(hero)
        session.commit()
        print(f"Hero with the id of {hero_id} has been deleted from the database")


def delete_a_team_obj(team_id: int):
    """
    i will pass the team id of the autoindex column
    and it will try to delete the row form the table
    """
    with Session(engine) as session:
        statement = select(TeamModel).where(TeamModel.id_ == team_id)
        results = session.exec(statement)
        team_row = results.one()
        session.delete(team_row)
        session.commit()
        print(f"The temm row of the id of {team_id} has been deleted from teh database")


if __name__ == "__main__":
    # create_db_and_tables()
    how_many = 5
    for _ in range(how_many):
        # create_hero()
        create_hero_and_team()
    # delete_a_hero_obj(hero_id=73)
    # delete_a_team_obj(team_id=3)
