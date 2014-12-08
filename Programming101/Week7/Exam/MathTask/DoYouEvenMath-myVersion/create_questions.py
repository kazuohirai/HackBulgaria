from sqlalchemy import Column, Integer, String
from create_base import Base


class Question(Base):
    __tablename__ = "question"
    id = Column(Integer, primary_key=True)
    question = Column(String)
    correct_answer = Column(String)

    def __str__(self):
        return "{}".format(self.question)

    def __repr__(self):
        return self.__str__()
