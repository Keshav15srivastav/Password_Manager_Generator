# password_gen.py

import random
import string

# Function to generate a strong password
def generate_password(length=12, include_uppercase=True, include_numbers=True, include_special_characters=True):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    numbers = string.digits if include_numbers else ''
    special_characters = string.punctuation if include_special_characters else ''

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + numbers + special_characters

    # Ensure at least one character from each selected set is included
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase_letters))
    if include_numbers:
        password.append(random.choice(numbers))
    if include_special_characters:
        password.append(random.choice(special_characters))
    
    # Fill the rest of the password length with random choices from the combined set
    while len(password) < length:
        password.append(random.choice(all_characters))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)
