#!/usr/bin/python3
"""Will define a new class for Cities"""

from models.base_model import BaseModel 

class Review(BaseModel):
    """Class Review that inherits from BaseModel"""

    place_id = "" """this will be place.id"""
    user_id = "" """user.id"""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
