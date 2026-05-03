"""
database_code/__init__.py
This file is saying this directory is a package
here i will write the database related codes
Tables > Models
Database realted functions and so on...
"""

from .hero_model import HeroModel
from .team_model import TeamModel

__all__ = [
    "HeroModel",
    "TeamModel",
]
