from sqlalchemy import Column, Integer, String, Float
from create_base import Base


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    rating = Column(Float)

    def __str__(self):
        return "{}| {} - {}".format(self.id, self.name, self.rating)

    def __repr__(self):
        return self.__str__()
