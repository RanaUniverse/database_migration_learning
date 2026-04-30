"""
here i will defines the tables in the form of class
of sqlmodel
"""

from sqlmodel import (
    Field,
    SQLModel,
)


class HeroModel(SQLModel, table=True):
    __tablename__ = "hero_data"  # type: ignore

    id_: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
