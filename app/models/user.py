from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from app.utils.db import db


class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.String, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=False, nullable=False)  # Not unique — duplicates allowed


    feedbacks = db.relationship('Feedback', back_populates='user')
