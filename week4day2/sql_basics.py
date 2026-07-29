import sqlite3
import os

DB_NAME = "section_practice.db"

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)


def section_1_sql_basics():
    "sql basics-create,where,orderby,limit"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        #CREATE
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
                role TEXT
            )
        """)

        #INSERT
        users_data=[
            ("Alice",25,"admin"),
            ("Bob",30,"editor"),
            ("Charlie",22,"viewer"),
            ("diana",28,"editor"),
            ("eve",35,"admin")
        ]
        cursor.executemany("INSERT INTO users (name,age,role) VALUES (?,?,?)",users_data)

        #selecting using where and order by in descending
        cursor.execute("SELECT name,age FROM users WHERE role = 'editor' ORDER BY age DESC")
        for row in cursor.fetchall():
            print(row)

        #limit and offset
        cursor.execute("SELECT name FROM users LIMIT 2 OFFSET 1")
        print(cursor.fetchall())

        #UPDATE
        cursor.execute("UPDATE users SET age = 26 WHERE name = 'Alice")

        #delete
        cursor.execute("DELETE FROM users WHERE name='Eve'")


def aggregations_and_joins():

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute("CREATE TABLE departments (id INTEGER PRIMARY KEY,dept_name TEXT)")
        cursor.execute("CREATE TABLE employees (id INTEGER PRIMARY KEY,name TEXT,salary INTEGER,dept_id INTEGER)")

        cursor.executemany("INSERT INTO departments (dept_name) VALUES (?)",[("HR",), ("Engineering"), ("Sales,",)])
        cursor.executemany("INSERT INTO employees (name,salary,dept_id) VALUES (?,?,?)",[
            ("John",50000,1),
            ("Jane",80000,2),
            ("Dev",90000,2),
            ("Sam",40000,NULL)
        ])
        
        #aggregations and group by
        print("\nAverage salary per department (Aggregations):")
        cursor.execute('''
            SELECT dept_id,COUNT(id),AVG(salary),MAX(salary)
            FROM employees
            GROUP BY dept_id
        ''')
        for row in cursor.fetchall():
            print(f"Dept {row[0]}:Count={row[1]},Avg Salary={row[2]}, Max Salary={row[3]}")

        



