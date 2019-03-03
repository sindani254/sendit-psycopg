import psycopg2
import os

DB_HOST = 'localhost'
DB_NAME = 'sendit'
DB_USERNAME = 'sindani254'
DB_PASS = 'Soen@30010010'
DB_PORT = '5432'

db_url = os.getenv('DB_URL')
print(db_url)

# creating the connection
try:
    con = psycopg2.connect(db_url)
except Exception as e:
    print(e)


# creating the cursor
cur = con.cursor()

# closing the connection
con.close()
