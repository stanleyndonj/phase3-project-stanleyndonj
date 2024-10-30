# lib/models/user.py
from sqlalchemy import Column, Integer, String
from . import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    # Relationship to FitnessGoal (one-to-many)
    fitness_goals = relationship('FitnessGoal', back_populates='user')

    def __repr__(self):
        return f"<User(name={self.name}, email={self.email})>"
