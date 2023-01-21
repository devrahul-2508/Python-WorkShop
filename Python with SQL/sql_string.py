from sqlalchemy import create_engine,text

db_string = "postgresql+psycopg2://postgres:rahul2508@localhost:5432/pythonworkshopdb"

db = create_engine(db_string)

# db.execute("CREATE TABLE IF NOT EXISTS films(title text,director text,year text)")
# db.execute("INSERT INTO films (title,director,year) VALUES ('Doctor Strange','Scott','2015')")

data = db.execute("SELECT * FROM films")
print(data.fetchall())

db.execute("UPDATE films SET title = 'Some2016film' WHERE year = '2016'")

#db.execute("DELETE FROM films WHERE year = '2016'")

print(db)