#!/usr/bin/python3
"""Module to create new users
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ class Users that inherit from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
