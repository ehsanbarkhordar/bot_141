

from sqlalchemy import Column, Integer, String

from bot.DataBase.models.base import Base


class StateCounter(Base):
    __tablename__ = "state_counter"
    id = Column(Integer, primary_key=True)
    state_name = Column(String)
    counter = Column(Integer)

    def __init__(self, state_name):
        self.state_name = state_name
        self.counter = 0
