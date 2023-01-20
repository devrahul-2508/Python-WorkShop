from sqlalchemy import create_engine
#rtsp

db_string = "postgresql+psycopg2://postgres:nirmalya2001@localhost:5432/pythonworkshopdb"

db = create_engine(db_string)

db.execute("CREATE TABLE IF NOT EXISTS flims (title TEXT, director TEXT, year TEXT)")
db.execute("INSERT INTO flims (title, director, year) VALUES ('Doctor Strange', 'Scott', '2016')")

data = db.execute("SELECT * FROM flims")

db.execute("UPDATE flims SET title='Some Flim' WHERE year='2015'")



print(data.fetchall())