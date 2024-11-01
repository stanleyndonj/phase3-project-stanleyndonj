from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine("sqlite:///football.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class League(Base):
    __tablename__ = 'leagues'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    country = Column(String)

    teams = relationship('Team', back_populates='league', cascade='all, delete-orphan')

    def __repr__(self):
        return f"League(id={self.id}, name='{self.name}', country='{self.country}')"

    @classmethod
    def create(cls, session, name, country):
        league = cls(name=name, country=country)
        session.add(league)
        session.commit()
        return league

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    def delete(self, session):
        session.delete(self)
        session.commit()

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    stadium = Column(String)
    league_id = Column(Integer, ForeignKey('leagues.id'))

    league = relationship('League', back_populates='teams')
    players = relationship('Player', back_populates='team', cascade='all, delete-orphan')

    def __repr__(self):
        return f"Team(id={self.id}, name='{self.name}', city='{self.city}', stadium='{self.stadium}')"

    @classmethod
    def create(cls, session, name, city, stadium, league_id):
        team = cls(name=name, city=city, stadium=stadium, league_id=league_id)
        session.add(team)
        session.commit()
        return team

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    def delete(self, session):
        session.delete(self)
        session.commit()

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    position = Column(String)
    team_id = Column(Integer, ForeignKey('teams.id'))

    team = relationship('Team', back_populates='players')

    def __repr__(self):
        return f"Player(id={self.id}, name='{self.name}', position='{self.position}')"

    @classmethod
    def create(cls, session, name, position, team_id):
        player = cls(name=name, position=position, team_id=team_id)
        session.add(player)
        session.commit()
        return player

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).get(id)

    def delete(self, session):
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)
