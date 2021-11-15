#!/usr/bin/python3
"""Will define a new class for First Users"""


from models.base_model import BaseModel


class User(BaseModel):
    """Class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
