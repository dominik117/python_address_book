import csv
from src.contact import Contact

class AddressBook:
    FILENAME = "address_book.csv"

    def __init__(self):
        self.contacts = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.FILENAME, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    self.contacts.append(Contact(row[0], row[1], row[2]))
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.FILENAME, 'w', newline='') as file:
            writer = csv.writer(file)
            for contact in self.contacts:
                writer.writerow([contact.name, contact.email, contact.phone])

    def add(self, contact):
        self.contacts.append(contact)
        self.save_to_file()

    def view_all(self):
        for contact in self.contacts:
            print(contact)

    def search(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def edit(self, name):
        contact = self.search(name)
        if contact:
            print(f"Editing {contact}...")
            new_name = input("Enter new name or press Enter to skip: ")
            new_email = input("Enter new email or press Enter to skip: ")
            new_phone = input("Enter new phone or press Enter to skip: ")

            if new_name:
                contact.name = new_name
            if new_email:
                contact.email = new_email
            if new_phone:
                contact.phone = new_phone

            self.save_to_file()
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete(self, name):
        contact = self.search(name)
        if contact:
            self.contacts.remove(contact)
            self.save_to_file()
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")