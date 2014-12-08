from sqlalchemy import Column, Integer, String
from create_base import Base


class Score(Base):
    __tablename__ = "score"
    id = Column(Integer, primary_key=True)
    handle = Column(String)
    highest_score = Column(Integer)

    def __str__(self):
        return "{} - {}".format(self.handle, self.highest_score)

    def __repr__(self):
        return self.__str__()
