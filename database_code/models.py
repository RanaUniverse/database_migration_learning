"""
here i will defines the tables in the form of class
of sqlmodel
"""

from typing import Optional
from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)


class HeroModel(SQLModel, table=True):
    __tablename__ = "hero_data"  # type: ignore

    id_: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    phone: str | None = None

    team_id: int | None = Field(default=None, foreign_key="team_data.id_")
    team: Optional["TeamModel"] = Relationship(back_populates="heroes")


class TeamModel(SQLModel, table=True):
    __tablename__ = "team_data"  # type: ignore

    id_: int = Field(default=None, primary_key=True)
    name: str
    headquarters: str

    heroes: list[HeroModel] = Relationship(back_populates="team")
