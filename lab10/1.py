import psycopg2

# connecting to a database

conn = psycopg2.connect(
    host="localhost", 
    dbname="suppliers", 
    user="postgres", 
    password="1234"
    )

# creating a cursor
# cursor is needed to interact with the database
cur = conn.cursor()

print('PostgreSQL database version:')
cur.execute('SELECT version()') # Executing the query inside the single quotes 
                                # in our connected database
db_ver = cur.fetchall() # Getting all data that we got from the last query
print(db_ver)