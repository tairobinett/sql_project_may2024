import psycopg2
import time
import os

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

sql = '''CREATE TABLE IF NOT EXISTS dice_rolls(
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(255),
    d2 INT,
    d3 INT,
    d4 INT, 
    d6 INT, 
    d8 INT,
    d10 INT, 
    d12 INT, 
    d20 INT, 
    d100 INT 
);'''

cursor.execute(sql)

print("Current active directory:", os.getcwd())
print("Contents of backend directory:", os.listdir("/app"))
print("Contents of dice-stats directory:", os.listdir("/app/dice-stats"))


sql = '''COPY dice_rolls 
    FROM '/app/dice-stats/data.csv' 
    DELIMITER ',' CSV HEADER;
'''

cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()
