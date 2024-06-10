from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import time
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world(): 
    return "<p>Hello World!</p>"

@app.route("/goodbye")
def gb_world(): 
    print("teststeststest")
    return "<p>Goodbye World!</p>"


@app.route("/create_table")
def create_table(): 
    tableName = request.args.get('tableName')
    # Retry connection to ensure DB is up
    print("start function")
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

    sql = f'''CREATE TABLE IF NOT EXISTS {tableName}(
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
    return jsonify({"status":"success", "tableName":tableName}), 200