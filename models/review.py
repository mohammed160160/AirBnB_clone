#!/usr/bin/python3
"""Review Module
This Module inherits from BaseModel class.
Review Module contains the attributes to be assigned
to the reviews created by the users.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class."""
    place_id = ""
    user_id = ""
    text = ""
