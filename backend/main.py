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


@app.route("/create_table", methods=['POST'])
def create_table(): 
    data = request.get_json()
    tableName = data.get('tableName')
    # tableName = request.args.get('tableName')
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
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        major VARCHAR(100)
    );'''

    cursor.execute(sql)

    connection.commit()
    return jsonify({"status":"success", "tableName":tableName}), 200


@app.route("/delete_table", methods=['POST'])
def delete_table(): 
    data = request.get_json()
    tableName = data.get('tableName')
    # tableName = request.args.get('tableName')
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

    sql = f'''DROP TABLE IF EXISTS {tableName};'''

    cursor.execute(sql)

    connection.commit()
    return jsonify({"status":"success", "tableName":tableName}), 200