from models import Base, engine

def reset_database():
    print("Dropping existing tables...")
    Base.metadata.drop_all(engine)
    print("Creating new tables...")
    Base.metadata.create_all(engine)
    print("Database reset complete.")

if __name__ == "__main__":
    reset_database()
