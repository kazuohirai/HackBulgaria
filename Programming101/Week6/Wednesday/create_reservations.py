from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import create_base


class Reservation(create_base.Base):
    __tablename__ = "reservations"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    projection_id = Column(Integer, ForeignKey("projections.id"))
    row = Column(Integer)
    col = Column(Integer)
    projection = relationship("Projection", backref="projection_id")

    def __str__(self):
        return "{} - ({}, {})".format(self.username, self.row, self.col)

    def __repr__(self):
        return self.__str__()
