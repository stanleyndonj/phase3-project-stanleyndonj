# lib/models/__init__.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Database setup
engine = create_engine('sqlite:///fitness_tracker.db')
Session = sessionmaker(bind=engine)
session = Session()

# Make sure to import all the models here so they can be created together
from .user import User
from .fitness_goal import FitnessGoal
from .progress import Progress

def create_tables():
    Base.metadata.create_all(engine)
# At the bottom of lib/models/__init__.py
if __name__ == "__main__":
    create_tables()
