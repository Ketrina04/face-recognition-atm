import sqlite3

def initialize_db():
    conn = sqlite3.connect("database/atm_users.db")
    cursor = conn.cursor()

    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            account_number TEXT NOT NULL UNIQUE,
            image_path TEXT
            CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    account_number TEXT UNIQUE,
    balance REAL,
    image_path TEXT
);

        )
    ''')

    conn.commit()
    conn.close()

def add_user(name, account_number, image_path):
    initialize_db()  
    conn = sqlite3.connect("database/atm_users.db")
    cursor = conn.cursor()

    try:
        cursor.execute('''
            INSERT INTO users (name, account_number, image_path)
            VALUES (?, ?, ?)
        ''', (name, account_number, image_path))

        conn.commit()
    except sqlite3.IntegrityError:
        print("Account number already exists in the database!")
    finally:
        conn.close()
