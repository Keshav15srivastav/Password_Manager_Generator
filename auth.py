# auth.py

import hashlib
import getpass
import json
import os
from encryption import encrypt_password, decrypt_password
from password_gen import generate_password
from database import store_password, retrieve_password, search_accounts

USER_DATA_FILE = 'users.json'

# Load user data from file
def load_users():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# Save user data to file
def save_users(users):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(users, file)

# Initialize users dictionary
users = load_users()

# Function to create a new user
def create_user(username, password):
    if username in users:
        print("Username already exists.")
        return False
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        users[username] = hashed_password
        save_users(users)
        print(f"User {username} created successfully.")
        return True

# Function to verify user credentials
def verify_user(username, password):
    if username not in users:
        print("Username does not exist.")
        return False
    else:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if users[username] == hashed_password:
            print("Login successful.")
            return True
        else:
            print("Login failed. Incorrect password.")
            return False

# Function to prompt user for login
def login():
    username = input("Username: ")
    password = getpass.getpass("Password: ")
    return verify_user(username, password)

# Function to prompt user for account creation
def register():
    username = input("Choose a username: ")
    password_choice = input("Do you want to [generate] a password or [choose] your own? ").strip().lower()
    
    if password_choice == "generate":
        length = int(input("Enter password length: "))
        include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_special_characters = input("Include special characters? (yes/no): ").strip().lower() == 'yes'
        
        password = generate_password(length, include_uppercase, include_numbers, include_special_characters)
        print(f"Generated password: {password}")
    else:
        password = getpass.getpass("Choose a password: ")

    return create_user(username, password)

# Function to store a password for a specific account
def store_account_password():
    username = input("Username: ")
    if verify_user(username, getpass.getpass("Password: ")):
        account = input("Account: ")
        password = getpass.getpass("Password to store: ")
        store_password(username, account, password)
        print("Password stored successfully.")

# Function to retrieve a password for a specific account
def retrieve_account_password():
    username = input("Username: ")
    if verify_user(username, getpass.getpass("Password: ")):
        account = input("Account: ")
        password = retrieve_password(username, account)
        if password:
            print(f"Retrieved password: {password}")
        else:
            print("No password found for this account.")

# Function to search for accounts
def search_for_accounts():
    username = input("Username: ")
    if verify_user(username, getpass.getpass("Password: ")):
        search_term = input("Enter search term for account: ")
        accounts = search_accounts(username, search_term)
        if accounts:
            print(f"Accounts found: {', '.join(accounts)}")
        else:
            print("No accounts found matching the search term.")

# Example usage
if __name__ == "__main__":
    while True:
        action = input("Do you want to [login], [register], [store], [retrieve], [search], or [exit]? ").strip().lower()
        if action == "login":
            if login():
                break
        elif action == "register":
            register()
        elif action == "store":
            store_account_password()
        elif action == "retrieve":
            retrieve_account_password()
        elif action == "search":
            search_for_accounts()
        elif action == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid action. Please choose 'login', 'register', 'store', 'retrieve', 'search', or 'exit'.")
