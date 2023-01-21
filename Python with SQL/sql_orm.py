from sqlalchemy import create_engine,Column,String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_string = "postgresql+psycopg2://postgres:rahul2508@localhost:5432/pythonworkshopdb"

db = create_engine(db_string)

base = declarative_base()

class FilmsORM(base):
    __tablename__ = 'films_orm'
    title = Column(String,primary_key = True)
    director = Column(String)
    year = Column(String)

# class Theatre(base):
#     __tablename__ = 'theatre'
#     theatre_name = Column(String,primary_key = True)
#     established = Column(String)
#     address = Column(String)


Session = sessionmaker(db)

sess = Session()

base.metadata.create_all(db)

# #Insert Data
film_one = FilmsORM(
    title = "Sheila ki Jawaani",
    director = "Suuny Leone",
    year = "2018"
)

# sess.add(film_one)
# sess.commit()

#Insert Data
# theatre = Theatre(
#     theatre_name = 'BioScope',
#     established = '2018',
#     address = 'City Cnetre Mall Haldia'
# )
# sess.add(theatre)
# sess.commit()

##Read from the table

films = sess.query(FilmsORM)

for film in films:
    print(film.title,film.director,film.year)

# ##Update
# film_one.title = "Some 2016Film"    
# sess.commit()

#Delete
sess.delete(film_one)
sess.commit()


