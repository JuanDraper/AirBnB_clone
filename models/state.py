#!/usr/bin/python3
"""Will define a new class for States"""

from models.base_model import BaseModel

class State(BaseModel):
    """Class State that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
