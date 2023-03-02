#!/usr/bin/env python3
"""Encrypting passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a hashed password
    Args:
        password (str): password to be hashed
    """
    enc = password.encode()
    hashed = hashpw(enc, bcrypt.gensalt())
    return hashed

def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check whether a passw is valid
    Args:
        hashed_password (bytes): hashed password
        password (str): password in string
    Return:
        bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
