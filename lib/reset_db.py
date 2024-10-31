from sqlalchemy import create_engine, MetaData
from models import Base, engine

def reset_database():
    # Connect to the existing database
    engine = create_engine("sqlite:///football.db", echo=True)
    
    # Create a metadata object to hold the schema
    meta = MetaData()
    
    # Reflect the tables from the existing database
    meta.reflect(bind=engine)
    
    # Drop all tables
    meta.drop_all(bind=engine)

    # Recreate all tables based on the current models
    Base.metadata.create_all(engine)
    
    print("Database reset complete.")

if __name__ == "__main__":
    reset_database()