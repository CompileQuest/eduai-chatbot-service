from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.utils.db import db

class Feedback(db.Model):
    __tablename__ = 'feedbacks'

    feedback_id = db.Column(db.String, primary_key=True, nullable=False)
    user_id = db.Column(db.String, db.ForeignKey('users.user_id'), nullable=False)
    feedback_text = db.Column(db.String, nullable=False)
    feedback_type = db.Column(db.String(10), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = db.relationship('User', back_populates='feedbacks')