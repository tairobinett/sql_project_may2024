import psycopg2 
  
conn = psycopg2.connect( 
    dbname="db", user='postgres',  
  password='Password1', host='127.0.0.1', port='5432'
) 
  
conn.autocommit = True
cursor = conn.cursor() 
  
sql = '''CREATE TABLE employees(emp_id int,emp_name varchar, \ 
salary decimal); '''
  
cursor.execute(sql) 
  
conn.commit() 
conn.close() 
