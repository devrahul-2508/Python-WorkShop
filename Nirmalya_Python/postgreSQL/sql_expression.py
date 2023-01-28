from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

db_string = "postgresql+psycopg2://postgres:nirmalya2001@localhost:5432/pythonworkshopdb"

db = create_engine(db_string)

meta = MetaData(db)

flim_table = Table(
    'flims_exp',
    meta,
    Column('title', String),
    Column('director', String),
    Column('year', String) 
)

with db.connect() as conn:
    #CREATE TABLE
    flim_table.create()
    insert_statement = flim_table.insert().values(
                       title = 'Doctor Strange',
                       director = 'Rohit Shetty',
                       year = '2050'
    )
    conn.execute(insert_statement)

    # READ FROM TABLE
    select_statement = flim_table.select()
    select_result = conn.execute(select_statement)

    for item in select_result:
        print(item)

    #UPDATE TABLE
    update_statement = flim_table.update().where(
        flim_table.c.year == '2050'
    ).values(title = 'Amazing Spiderman')

    conn.execute(update_statement)

    #DELETE TABLE
    delete_statement = flim_table.delete().where(flim_table.c.year == '2050')
    conn.execute(delete_statement)