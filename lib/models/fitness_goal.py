# lib/models/fitness_goal.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class FitnessGoal(Base):
    __tablename__ = 'fitness_goals'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    target = Column(String, nullable=False)
    target_type = Column(String, nullable=False)
    date_created = Column(DateTime, default=datetime.utcnow)

    # ForeignKey linking to User
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    
    # Relationship to User (many-to-one)
    user = relationship('User', back_populates='fitness_goals')

    # Relationship to Progress (one-to-many)
    progress_entries = relationship('Progress', back_populates='goal')

    def __repr__(self):
        return f"<FitnessGoal(name={self.name}, target={self.target})>"
