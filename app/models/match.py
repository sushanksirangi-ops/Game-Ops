from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.database import Base


class Match(Base):

    __tablename__ = "matches"

    id = Column(Integer, primary_key=True)

    player_id = Column(String, nullable=False)
    match_id = Column(String, nullable=False)

    region = Column(String)
    device = Column(String)

    ping = Column(Integer)

    score = Column(Integer)

    kills = Column(Integer)

    deaths = Column(Integer)

    match_duration_seconds = Column(Integer)