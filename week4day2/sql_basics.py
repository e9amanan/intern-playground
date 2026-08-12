import os
import sqlite3

DB_NAME = "section_practice.db"

if os.path.exists(DB_NAME):
    os.remove(DB_NAME)


def section_1_sql_basics():
    "sql basics-create,where,orderby,limit"

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # CREATE
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER
                role TEXT
            )
        """)

        # INSERT
        users_data = [
            ("Alice", 25, "admin"),
            ("Bob", 30, "editor"),
            ("Charlie", 22, "viewer"),
            ("diana", 28, "editor"),
            ("eve", 35, "admin"),
        ]
        cursor.executemany(
            "INSERT INTO users (name,age,role) VALUES (?,?,?)", users_data
        )

        # selecting using where and order by in descending
        cursor.execute(
            "SELECT name,age FROM users WHERE role = 'editor' ORDER BY age DESC"
        )
        for row in cursor.fetchall():
            print(row)

        # limit and offset
        cursor.execute("SELECT name FROM users LIMIT 2 OFFSET 1")
        print(cursor.fetchall())

        # UPDATE
        cursor.execute("UPDATE users SET age = 26 WHERE name = 'Alice")

        # delete
        cursor.execute("DELETE FROM users WHERE name='Eve'")


def aggregations_and_joins():

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        cursor.execute(
            "CREATE TABLE departments (id INTEGER PRIMARY KEY,dept_name TEXT)"
        )
        cursor.execute(
            "CREATE TABLE employees (id INTEGER PRIMARY KEY,name TEXT,salary INTEGER,dept_id INTEGER)"
        )

        cursor.executemany(
            "INSERT INTO departments (dept_name) VALUES (?)",
            [("HR",), ("Engineering"), ("Sales,",)],
        )
        cursor.executemany(
            "INSERT INTO employees (name,salary,dept_id) VALUES (?,?,?)",
            [
                ("John", 50000, 1),
                ("Jane", 80000, 2),
                ("Dev", 90000, 2),
                ("Sam", 40000, None),
            ],
        )

        # aggregations and group by
        print("\nAverage salary per department (Aggregations):")
        cursor.execute("""
            SELECT dept_id,COUNT(id),AVG(salary),MAX(salary)
            FROM employees
            GROUP BY dept_id
        """)
        for row in cursor.fetchall():
            print(
                f"Dept {row[0]}:Count={row[1]},Avg Salary={row[2]}, Max Salary={row[3]}"
            )
            print("\nINNER JOIN (Employees with their departments):")
        cursor.execute("""
            SELECT employees.name, departments.dept_name 
            FROM employees 
            INNER JOIN departments ON employees.dept_id = departments.id
        """)
        print(cursor.fetchall())

        # 3. LEFT JOIN (Returns ALL employees, even if dept_name is NULL)
        print("\nLEFT JOIN (All employees, including Sam who has no dept):")
        cursor.execute("""
            SELECT employees.name, departments.dept_name 
            FROM employees 
            LEFT JOIN departments ON employees.dept_id = departments.id
        """)
        print(cursor.fetchall())


def section_3_constraints_and_relationships():
    """
    SYLLABUS: Constraints (PK, FK, UNIQUE, NOT NULL, CHECK, DEFAULT) & Relationships (1:N, M:N)
    """
    print("\n--- SECTION 3: CONSTRAINTS & RELATIONSHIPS ---")

    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            "PRAGMA foreign_keys = 1"
        )  # MUST turn this on in SQLite to enforce FKs
        cursor = conn.cursor()

        # Table 1: Authors (One side of the 1:N relationship)
        # Demonstrates: PRIMARY KEY, NOT NULL, UNIQUE
        cursor.execute("""
            CREATE TABLE authors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL
            )
        """)

        # Table 2: Books (Many side of the 1:N relationship)
        # Demonstrates: FOREIGN KEY, DEFAULT, CHECK
        cursor.execute("""
            CREATE TABLE books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author_id INTEGER,
                status TEXT DEFAULT 'draft' CHECK(status IN ('draft', 'published')),
                FOREIGN KEY (author_id) REFERENCES authors(id)
            )
        """)

        # Insert Valid Data
        cursor.execute(
            "INSERT INTO authors (email, name) VALUES ('writer@test.com', 'Stephen')"
        )
        author_id = cursor.lastrowid
        cursor.execute(
            "INSERT INTO books (title, author_id) VALUES ('The Shining', ?)",
            (author_id,),
        )

        # Constraint Test 1: UNIQUE constraint failure
        try:
            cursor.execute(
                "INSERT INTO authors (email, name) VALUES ('writer@test.com', 'King')"
            )
        except sqlite3.IntegrityError as e:
            print(f"Caught Expected UNIQUE Error: {e}")

        # Constraint Test 2: CHECK constraint failure
        try:
            cursor.execute(
                "INSERT INTO books (title, author_id, status) VALUES ('IT', ?, 'invalid')'",
                (author_id,),
            )
        except sqlite3.IntegrityError as e:
            print(f"Caught Expected CHECK Error: {e}")

        # Constraint Test 3: FOREIGN KEY constraint failure (Author ID 999 doesn't exist)
        try:
            cursor.execute(
                "INSERT INTO books (title, author_id) VALUES ('Misery', 999)"
            )
        except sqlite3.IntegrityError as e:
            print(f"Caught Expected FOREIGN KEY Error: {e}")


def section_4_indexes():
    """
    SYLLABUS: Indexes (CREATE INDEX, EXPLAIN QUERY PLAN)
    """
    print("\n--- SECTION 4: INDEXES ---")

    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()

        # Create a table and insert a row
        cursor.execute(
            "CREATE TABLE products (id INTEGER PRIMARY KEY, sku TEXT, price REAL)"
        )
        cursor.execute("INSERT INTO products (sku, price) VALUES ('ABC-123', 19.99)")

        # 1. EXPLAIN QUERY PLAN BEFORE Index
        cursor.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM products WHERE sku = 'ABC-123'"
        )
        print("Query Plan WITHOUT Index (Notice it says 'SCAN TABLE'):")
        print(cursor.fetchall())

        # 2. CREATE INDEX
        print("\nCreating Index on SKU column...")
        cursor.execute("CREATE INDEX idx_products_sku ON products(sku)")

        # 3. EXPLAIN QUERY PLAN AFTER Index
        cursor.execute(
            "EXPLAIN QUERY PLAN SELECT * FROM products WHERE sku = 'ABC-123'"
        )
        print("Query Plan WITH Index (Notice it says 'SEARCH TABLE' using the index):")
        print(cursor.fetchall())


def section_5_transactions_and_sqlite3():
    """
    SYLLABUS: Transactions (ACID, BEGIN, COMMIT, ROLLBACK) & python sqlite3 features
    """
    print("\n--- SECTION 5: TRANSACTIONS & SQLITE3 ---")

    # We create a specific connection to demonstrate manual transaction control
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE bank_accounts (name TEXT, balance INTEGER CHECK(balance >= 0))"
    )
    cursor.execute("INSERT INTO bank_accounts VALUES ('Alice', 100), ('Bob', 50)")
    conn.commit()  # Save initial state

    print("\nAttempting a bank transfer (Alice sends $200 to Bob)...")

    try:
        # SQLite automatically starts a transaction when executing DML (Data Manipulation Language)

        # Step 1: Deduct from Alice (This will FAIL because 100 - 200 = -100, violating CHECK >= 0)
        cursor.execute(
            "UPDATE bank_accounts SET balance = balance - 200 WHERE name = 'Alice'"
        )

        # Step 2: Add to Bob (This code won't run because Step 1 throws an error)
        cursor.execute(
            "UPDATE bank_accounts SET balance = balance + 200 WHERE name = 'Bob'"
        )

        conn.commit()
        print("Transfer Successful!")

    except sqlite3.IntegrityError as e:
        print(f"Transfer Failed due to constraint violation: {e}")
        conn.rollback()  # THIS IS CRUCIAL: Reverts Step 1 if Step 2 fails!
        print("Transaction Rolled Back safely.")

    # Verify data wasn't partially updated
    cursor.execute("SELECT * FROM bank_accounts")
    print("Final Account Balances (Should be unchanged):", cursor.fetchall())

    conn.close()
