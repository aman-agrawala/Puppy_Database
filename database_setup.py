import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
	__tablename__ = 'Shelter'

	name = Column(String(80), nullable = False)
	address = Column(String(250))
	city = Column(String(250))
	state = Column(String(80))
	zipCode = Column(Integer)
	website = Column(String(250))
	id = Column(Integer, primary_key = True)

class Puppy(Base):
	__tablename__ = 'Puppy'

	name = Column(String(250), nullable = False)
	dob = Column(Date, nullable = False)
	gender = Column(String(80), nullable = False)
	weight = Column(Integer)
	shelter_id = Column(Integer, ForeignKey('Shelter.id'))
	shelter = relationship(Shelter)

engine = create_engine('sqlite:///puppies.db')

Base.metadata.create_all(engine)
