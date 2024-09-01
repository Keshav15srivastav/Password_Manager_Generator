# database.py

import sqlite3
from encryption import encrypt_password, decrypt_password

DATABASE_FILE = 'passwords.db'

# Function to initialize the database
def initialize_database():
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            account TEXT NOT NULL,
            encrypted_password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to store an encrypted password
def store_password(username, account, password):
    encrypted_password = encrypt_password(password)
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
        INSERT INTO passwords (username, account, encrypted_password)
        VALUES (?, ?, ?)
    ''', (username, account, encrypted_password))
    conn.commit()
    conn.close()

# Function to retrieve an encrypted password
def retrieve_password(username, account):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT encrypted_password FROM passwords
        WHERE username = ? AND account = ?
    ''', (username, account))
    result = c.fetchone()
    conn.close()
    if result:
        return decrypt_password(result[0])
    else:
        return None

# Function to search for accounts by a search term
def search_accounts(username, search_term):
    conn = sqlite3.connect(DATABASE_FILE)
    c = conn.cursor()
    c.execute('''
        SELECT account FROM passwords
        WHERE username = ? AND account LIKE ?
    ''', (username, f'%{search_term}%'))
    results = c.fetchall()
    conn.close()
    return [result[0] for result in results]

# Initialize the database when the module is imported
initialize_database()
