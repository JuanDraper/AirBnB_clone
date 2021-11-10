#!/usr/bin/python3
"""Will define a new class for Cities"""

from models.base_model import BaseModel 

class City(BaseModel):
    """Class City that inherits from BaseModel"""

    state_id = "" """this will be State.id"""
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
