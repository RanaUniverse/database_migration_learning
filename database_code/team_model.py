"""
database_code/team_model.py
Here i will write the code related to the team table
"""

from typing import (
    # on execution time this is false but for type checking true
    TYPE_CHECKING,
)

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

if TYPE_CHECKING:
    from .hero_model import HeroModel


class TeamModel(SQLModel, table=True):
    __tablename__ = "team_data"  # type: ignore

    id_: int = Field(default=None, primary_key=True)
    name: str
    headquarters: str

    heroes: list["HeroModel"] = Relationship(
        back_populates="team",
        cascade_delete=True,
    )
