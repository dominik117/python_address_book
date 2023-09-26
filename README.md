# Address Book using Python

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Getting Started](#getting-started)
4. [Features](#features)
5. [Error Handling](#error-handling)
6. [Future Enhancements](#future-enhancements)
7. [Contributing](#contributing)
8. [License](#license)

## Overview
This project is a simple CLI-based address book application. Users can perform operations such as adding a new contact, viewing all contacts, searching, editing, and deleting a contact. Contacts are stored in a CSV file (`address_book.csv`), ensuring data persistence across sessions.

## Project Structure
- **main.py**: The main driver of the application, providing an interactive CLI menu for users to perform various contact-related operations.
- **contact.py**: Contains the `Contact` class representing an individual contact with attributes: name, email, and phone number.
- **address_book.py**: Contains the `AddressBook` class responsible for managing contacts, including adding, editing, deleting, viewing, and saving contacts to and from the CSV file.

## Getting Started

1. Ensure Python is installed on your machine.
2. Clone the project repository or download the source code.
3. Navigate to the project directory in your terminal.
4. Run the application with the following command:
```shell
python main.py
```
5. Follow the on-screen prompts to perform various operations on the address book.

## Features

1. **Add a New Contact**: Allows the user to add a new contact by entering the name, email, and phone number.
2. **View All Contacts**: Displays a list of all contacts in the address book.
3. **Search for a Contact**: Enables searching for a contact by name.
4. **Edit a Contact**: Allows modifying the name, email, or phone number of an existing contact.
5. **Delete a Contact**: Removes an existing contact from the address book.
6. **Exit**: Closes the application.

## Error Handling
The program provides feedback and guidance for incorrect actions, such as trying to edit a non-existent contact.

## Future Enhancements
- Implement advanced search functionality allowing searches by email or phone in addition to name.
- Implement input validation for email and phone.
- Add an option for backing up the address book to cloud storage.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change. Please ensure to update tests as appropriate.

## License
This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).