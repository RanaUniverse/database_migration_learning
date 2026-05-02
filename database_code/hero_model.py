"""
database_code/hero_model.py
Here i will write the code related to the hero table
"""

from typing import (
    # on execution time this is false but for type checking true
    TYPE_CHECKING,
    Optional,
)

from sqlmodel import (
    Field,
    SQLModel,
    Relationship,
)

if TYPE_CHECKING:
    from .team_model import TeamModel


class HeroModel(SQLModel, table=True):
    __tablename__ = "hero_data"  # type: ignore

    id_: int = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None
    phone: str | None = None

    team_id: int | None = Field(default=None, foreign_key="team_data.id_")
    team: Optional["TeamModel"] = Relationship(back_populates="heroes")
