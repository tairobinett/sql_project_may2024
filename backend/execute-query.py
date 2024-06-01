import psycopg2
import time

# Retry connection to ensure DB is up
while True:
    try:
        connection = psycopg2.connect(
            dbname='mydb',
            user='postgres',
            password='Password1',
            host='db',
            port='5432'
        )
        break
    except psycopg2.OperationalError:
        print("Database not ready, retrying in 5 seconds...")
        time.sleep(5)

cursor = connection.cursor()

sql = '''CREATE TABLE IF NOT EXISTS employees(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(255),
    salary DECIMAL
);'''

cursor.execute(sql)
connection.commit()
cursor.close()
connection.close()
