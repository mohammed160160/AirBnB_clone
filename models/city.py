#!/usr/bin/python3
"""City Module
This Module inherits from BaseModel class.
City Module contains the attributes to be assigned
to the cities.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class."""
    state_id = ""
    name = ""
