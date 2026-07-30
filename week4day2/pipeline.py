import sqlite3
import json
from validators import DataValidator
from database_practice import setup_database

def etl_pipeline(csv_path, db_name):
    print("--- Starting ETL Pipeline ---")
    
    # 1. EXTRACT & TRANSFORM (Validation)
    print("Extracting and Validating data...")
    validator = DataValidator()
    clean_data = validator.validate_task_csv(csv_path)
    
    if validator.errors:
        print(f"Validation finished with {len(validator.errors)} errors:")
        for err in validator.errors:
            print(f"  Row {err['row']} | Field '{err['field']}': {err['error']}")
        
    
    print(f"Successfully extracted {len(clean_data)} valid records.")
    
    # 2. LOAD (Database & JSON)
    if clean_data:
        print("Loading to SQLite (with transactions)...")
        setup_database(db_name) 
        
        # Load to JSON as a backup/alternative format
        with open('validated_tasks.json', 'w') as f:
            json.dump(clean_data, f, indent=4)
            
        try:
            with sqlite3.connect(db_name) as conn:
                conn.execute("PRAGMA foreign_keys = ON")
                cursor = conn.cursor()
                
                
                for task in clean_data:
                   
                    cursor.execute('''
                        INSERT INTO tasks (title, description, status) 
                        VALUES (?, ?, ?)
                    ''', (task['title'], task['description'], task['status']))
                    
                    task_id = cursor.lastrowid
                   
                    for cat_name in task['categories']:
                        cursor.execute('INSERT OR IGNORE INTO categories (name) VALUES (?)', (cat_name,))
                        cursor.execute('SELECT id FROM categories WHERE name = ?', (cat_name,))
                        cat_id = cursor.fetchone()[0]
                        
                        cursor.execute('''
                            INSERT INTO tasks_categories (task_id, category_id) 
                            VALUES (?, ?)
                        ''', (task_id, cat_id))
                        
            print("Successfully loaded data into SQLite database.")
        except Exception as e:
            print(f"CRITICAL ERROR during LOAD: {e}")
            print("Entire database transaction has been rolled back.")

if __name__ == "__main__":
    # Create a dummy CSV for testing
    with open('test_input.csv', 'w') as f:
        f.write("title,description,status,categories,due_date\n")
        f.write("Setup Django,Initial config,done,Python,2026-08-01\n")
        f.write(",Empty title test,todo,Error,2026-08-02\n") # Will fail validation
        f.write("Learn Views,Write class based views,invalid_stat,Django,\n") # Will fail validation
        f.write("Database Models,Write ORM classes,in_progress,\"Django,SQL\",2026-08-05\n")

    etl_pipeline('test_input.csv', 'etl_target.db')