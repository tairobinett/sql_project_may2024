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
    die_type INT,
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

connection.commit()

#print("Current active directory:", os.getcwd())
#print("Contents of backend directory:", os.listdir("/app"))
#print("Contents of dice-stats directory:", os.listdir("/app/dice-stats"))

csv_file_path = '/app/dice-stats/data.csv'
if os.path.exists(csv_file_path):
    with open(csv_file_path, 'r') as f:
        sql_copy = '''COPY dice_rolls(die_type, d2, d3, d4, d6, d8, d10, d12, d20, d100) FROM STDIN WITH CSV HEADER DELIMITER ',';'''
        cursor.copy_expert(sql_copy, f)
    print("Data copied from CSV file to 'dice_rolls' table.")
else:
    print(f"CSV file '{csv_file_path}' does not exist.")

#sql = '''COPY dice_rolls 
#    FROM '/app/dice-stats/data.csv' 
#    DELIMITER ',' CSV HEADER;
#'''

#cursor.execute(sql)

connection.commit()
cursor.close()
connection.close()
