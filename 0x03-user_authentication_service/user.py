#!/usr/bin/env python3
"""class User"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    """representation of class user"""
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(250), nullable=False, unique=True, index=True)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
