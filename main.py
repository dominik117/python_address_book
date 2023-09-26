import csv
from src.address_book import AddressBook
from src.contact import Contact

def main():
    address_book = AddressBook()
    while True:
        print("\n--- Address Book ---")
        print("1. Add a new contact")
        print("2. View all contacts")
        print("3. Search for a contact")
        print("4. Edit a contact")
        print("5. Delete a contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter the name: ")
            email = input("Enter the email: ")
            phone = input("Enter the phone number: ")
            address_book.add(Contact(name, email, phone))
            print(f"Contact {name} added successfully!")

        elif choice == "2":
            address_book.view_all()

        elif choice == "3":
            name = input("Enter the name to search: ")
            contact = address_book.search(name)
            if contact:
                print(contact)
            else:
                print("Contact not found!")

        elif choice == "4":
            name = input("Enter the name of the contact to edit: ")
            address_book.edit(name)

        elif choice == "5":
            name = input("Enter the name of the contact to delete: ")
            address_book.delete(name)

        elif choice == "6":
            print("Closing...")
            break

        else:
            print("Invalid choice! Please choose a valid option.")


if __name__ == "__main__":
    main()
