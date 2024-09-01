# encryption.py

from cryptography.fernet import Fernet
import base64
import os

# Function to generate a key for encryption
def generate_key():
    key = Fernet.generate_key()
    with open('secret.key', 'wb') as key_file:
        key_file.write(key)

# Function to load the key from file
def load_key():
    return open('secret.key', 'rb').read()

# Generate a key if it does not exist
if not os.path.exists('secret.key'):
    generate_key()

# Load the key
key = load_key()
fernet = Fernet(key)

# Function to encrypt a password
def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

# Function to decrypt a password
def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()
