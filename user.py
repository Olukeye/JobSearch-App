from flask import request, jsonify, Response
from sqlalchemy import Column, Integer, String, Boolean, BigInteger, ForeignKey
from date_stuff import create_customised_datetime
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship
from database import get_db, Base
from sqlalchemy.orm import Session
from typing import Dict, Optional
from pydantic import User


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = column(String, nullable=False)
    created_at = Column(String, nullable=False)
    
    
def add_user(db: Session, user:User):
    