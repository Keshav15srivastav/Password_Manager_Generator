# Password_Manager_Generator

Project Overview

This project is a command-line-based secure password manager that allows users to store and retrieve their passwords for different accounts. The application uses encryption to securely store passwords, ensuring that they are protected from unauthorized access. 

Key Features

- User Authentication and Authorization: Secure login and user verification.
- Password Encryption and Security: Industry-standard AES encryption for storing passwords.
- Password Generation: Option to generate strong, unique passwords.
- Database Management: Store and retrieve encrypted passwords using SQLite.
- Backup and Sync: Potential for future implementation of backup and synchronization features.

Project Structure

```
.
├── auth.py              # Handles user authentication and authorization
├── encryption.py        # Manages password encryption and decryption
├── password_gen.py      # Generates strong passwords based on user specifications
├── database.py          # Manages the storage and retrieval of passwords from the database
├── passwords.db         # SQLite database file for storing encrypted passwords
├── secret.key           # Encryption key file (automatically generated)
├── requirements.txt     # Python dependencies for the project
└── README.md            # Project documentation (this file)
```

Installation

 ~ Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtual environment (optional but recommended)

Steps

1. Clone the Repository:

    ```sh
    git clone https://github.com/Keshav15srivastav/password-manager-generator.git
    cd secure-password-manager
    ```

2. Create a Virtual Environment (Optional):

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    ```

3. Install Dependencies:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the Application:

    ```sh
    python auth.py
    ```

Usage

- Register a New User: Run `auth.py` and select the "register" option to create a new user account.
- Login: Run `auth.py` and select the "login" option. Once logged in, you can store and retrieve your passwords.
- Store Passwords: After logging in, you can choose to store passwords for different accounts.
- Retrieve Passwords: Retrieve your stored passwords using your account credentials.

Security Considerations

- Encryption: All passwords are encrypted using AES encryption before being stored in the SQLite database.
- Key Management: The encryption key is stored in a separate file (`secret.key`). Ensure that this file is kept secure and not shared.

Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any improvements or bug fixes.

License

This project is licensed under the MIT License - see the (LICENSE) file for details.

Future Improvements

- Implement a GUI version of the password manager.
- Add support for biometric authentication.
- Implement cloud backup and synchronization features.

Contact

For any inquiries or issues, please reach out to (keshavsrivastavgbh@gmail.com).

