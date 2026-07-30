import sqlite3
import datetime

# 1. Schema Definition (Create tables with constraints and indexes)
def setup_database(db_name='tasks.db'):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        
        # Categories Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        ''')
        
        # Tasks Table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT NOT NULL CHECK(status IN ('todo', 'in_progress', 'done')),
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Junction Table for Many-to-Many relationship
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks_categories (
                task_id INTEGER,
                category_id INTEGER,
                PRIMARY KEY (task_id, category_id),
                FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
                FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
            )
        ''')
        
        # Indexes
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_tasks_status ON tasks(status)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_tasks_created_at ON tasks(created_at)')
        
        conn.commit()
        print("Database schema and indexes created successfully.")

# 2. CRUD Operations with Transactions
def add_task_with_categories(db_name, title, desc, status, category_names):
    """Example of a transaction handling multiple inserts"""
    try:
        # Context manager handles commit/rollback automatically
        with sqlite3.connect(db_name) as conn:
            # Enable foreign key support in SQLite (off by default)
            conn.execute("PRAGMA foreign_keys = ON")
            cursor = conn.cursor()
            
            # Insert Task
            cursor.execute('''
                INSERT INTO tasks (title, description, status) 
                VALUES (?, ?, ?)
            ''', (title, desc, status))
            
            task_id = cursor.lastrowid
            
            # Handle Categories
            for cat_name in category_names:
                # Insert category if it doesn't exist, ignore if it does
                cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (cat_name,))
                
                # Fetch the category ID (whether just inserted or already existed)
                cursor.execute('SELECT id FROM categories WHERE name = ?', (cat_name,))
                cat_id = cursor.fetchone()[0]
                
                # Link task and category
                cursor.execute('''
                    INSERT INTO tasks_categories (task_id, category_id) 
                    VALUES (?, ?)
                ''', (task_id, cat_id))
                
            print(f"Task '{title}' added successfully with categories.")
            
    except sqlite3.IntegrityError as e:
        print(f"Database Integrity Error: {e}. Transaction rolled back.")
    except Exception as e:
        print(f"An error occurred: {e}. Transaction rolled back.")

if __name__ == "__main__":
    db = 'practice.db'
    setup_database(db)
    add_task_with_categories(db, "Learn ETL", "Build a Python pipeline", "in_progress", ["Data Engineering", "Python"])
    add_task_with_categories(db, "Bad Task", "Fails check constraint", "invalid_status", ["Testing"]) # This will rollback