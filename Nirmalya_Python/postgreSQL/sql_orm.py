from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql+psycopg2://postgres:nirmalya2001@localhost:5432/pythonworkshopdb"
db = create_engine(db_string)
base = declarative_base()


class FlimsOrm(base):
    __tablename__ = 'flims_orm'
    title = Column(String, primary_key=True)
    director = Column(String)
    year = Column(String)

class Theatre(base):
    __tablename__ = 'theatre'
    theatre_name = Column(String, primary_key=True)
    establised = Column(String)
    address = Column(String)

Session = sessionmaker(db)
sess = Session()

base.metadata.create_all(db)

#INSERT DATA TO THE FLIMS TABLE
flim_one = FlimsOrm(
    title = "Doctor Strange",
    director = "Nick",
    year = "2019"
)
sess.add(flim_one)
sess.commit()

# INSERT TO THE THRETRE TABLE
theatre_one = Theatre(
    theatre_name = 'Inox',
    establised = '2016',
    address = 'India'
)
sess.add(theatre_one)
sess.commit()

# READ FROM FLIMS TABLE
flims = sess.query(FlimsOrm)
for flim in flims:
    print(flim.title)

threaters = sess.query(Theatre)
for threatre in threaters:
    print(threatre.theatre_name)

# UPDATE 
flim_one.title = "Updated"
sess.commit()

# Delete
sess.delete(flim_one)
sess.commit()