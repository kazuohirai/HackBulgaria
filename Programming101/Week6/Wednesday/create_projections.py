from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import create_base


class Projection(create_base.Base):
    __tablename__ = "projections"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    movie_type = Column(String)
    time = Column(String)
    date = Column(String)
    movie = relationship("Movie", backref="movie_id")

    def __str__(self):
        return "{}| {} - {}".format(self.id, self.movie_type, self.time)

    def __repr__(self):
        return self.__str__()
