#!/usr/bin/python3
"""Will define a new class for Amenities"""


from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class Amenity that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
