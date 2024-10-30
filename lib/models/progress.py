# lib/models/progress.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from . import Base

class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.utcnow)
    value = Column(String, nullable=False)
    notes = Column(String)

    # ForeignKey linking to FitnessGoal
    goal_id = Column(Integer, ForeignKey('fitness_goals.id'), nullable=False)

    # Relationship to FitnessGoal (many-to-one)
    goal = relationship('FitnessGoal', back_populates='progress_entries')

    def __repr__(self):
        return f"<Progress(date={self.date}, value={self.value})>"
