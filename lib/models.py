from sqlalchemy import create_engine, Column, Integer, String,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship


engine = create_engine("sqlite:///football.db", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String)
    stadium = Column(String)

    players = relationship('Player', back_populates='team', cascade='all, delete-orphan')

    def __repr__(self):
        return "Team(name='{}', city='{}', stadium='{}')".format(self.name, self.city, self.stadium)

    @classmethod
    def create(cls, session, name, city, stadium):
        new_team = cls(name=name, city=city, stadium=stadium)
        session.add(new_team)
        session.commit()
        return new_team

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

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
        return "Player(name='{}', position='{}')".format(self.name, self.position)

    @classmethod
    def create(cls, session, name, position, team_id):
        new_player = cls(name=name, position=position, team_id=team_id)
        session.add(new_player)
        session.commit()
        return new_player

    @classmethod
    def get_all(cls, session):
        return session.query(cls).all()

    @classmethod
    def find_by_id(cls, session, id):
        return session.query(cls).filter_by(id=id).first()

    def get_team(self, session):
        return Team.find_by_id(session, self.team_id)

    def delete(self, session):
        session.delete(self)
        session.commit()

Base.metadata.create_all(engine)