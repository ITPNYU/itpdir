from sqlalchemy import Table #Boolean, Column, ForeignKey, Integer, String, Table, Text
#from sqlalchemy.dialects.mysql import TINYINT
from sqlalchemy.orm import relationship
from itpdir.database import Base, engine

# ORM classes
class Person(Base):
    __tablename__ = 'nyu_official'
    __table__ = Table(__tablename__, Base.metadata, autoload=True, autoload_with=engine)

    def __repr__(self):
        return '<Person %r>' % (self.netid)
