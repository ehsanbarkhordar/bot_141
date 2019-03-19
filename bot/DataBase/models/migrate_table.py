from sqlalchemy import Column, Integer

from bot.DataBase.models.base import Base


class Migrate(Base):
    __tablename__ = "migrate"
    id = Column(Integer, primary_key=True)
    is_migrated = Column(Integer)

    def __init__(self):
        self.is_migrated = 1
