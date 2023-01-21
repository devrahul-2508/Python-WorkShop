from sqlalchemy import create_engine,text,Table,Column,String,MetaData

db_string = "postgresql+psycopg2://postgres:rahul2508@localhost:5432/pythonworkshopdb"

db = create_engine(db_string)

meta = MetaData(db)

film_table = Table(
    'films_exp',
    meta,
    Column('title', String),
    Column('director',String),
    Column('year',String)
)

with db.connect() as conn:
    #CREATE TABLE 
    # film_table.create()
    # insert_statement = film_table.insert().values(
    #     title = "Doctor Strange",
    #     director = "Rohit Shetty",
    #     year = "2050"
    # )

    # conn.execute(insert_statement)

    #READ FROM TABLE
    select_statement = film_table.select()

    select_result = conn.execute(select_statement)

    for r in select_result:
        print(r)


    #UPDATE TABLE

    update_statement = film_table.update().where(
        film_table.c.year == '2050'
    ).values(title = "Amazing Spiderman")    

    conn.execute(update_statement)

    #Delete

    delete_statement = film_table.delete().where(
        film_table.c.year == '2050'
    )

    conn.execute(delete_statement)