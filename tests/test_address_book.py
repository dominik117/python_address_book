import unittest
import sys
sys.path.append('../src')
from src.address_book import AddressBook
from src.contact import Contact


class TestAddressBook(unittest.TestCase):

    def setUp(self):
        self.address_book = AddressBook()
        self.original_contacts = self.address_book.contacts.copy()
        # Cleanup the address for testing
        self.address_book.contacts = []
        self.address_book.save_to_file()

    def tearDown(self):
        # Revert the original address book
        self.address_book.contacts = self.original_contacts
        self.address_book.save_to_file()

    def test_add_contact(self):
        contact = Contact('John Doe', 'john@example.com', '1234567890')
        self.address_book.add(contact)
        self.assertEqual(len(self.address_book.contacts), 1)
        self.assertEqual(self.address_book.contacts[0], contact)

    def test_search_contact(self):
        contact = Contact('John Doe', 'john@example.com', '1234567890')
        self.address_book.add(contact)
        found_contact = self.address_book.search('John Doe')
        self.assertEqual(found_contact, contact)
        
    def test_edit_contact(self):
        contact = Contact('John Doe', 'john@example.com', '1234567890')
        self.address_book.add(contact)
        contact.name = 'Jane Doe'
        contact.email = 'jane@example.com'
        contact.phone = '0987654321'
        self.address_book.save_to_file()
        
        edited_contact = self.address_book.search('Jane Doe')
        self.assertEqual(edited_contact.name, 'Jane Doe')
        self.assertEqual(edited_contact.email, 'jane@example.com')
        self.assertEqual(edited_contact.phone, '0987654321')
        
    def test_delete_contact(self):
        contact = Contact('John Doe', 'john@example.com', '1234567890')
        self.address_book.add(contact)
        self.address_book.delete('John Doe')
        self.assertEqual(len(self.address_book.contacts), 0)


if __name__ == '__main__':
    unittest.main()

# python -m unittest tests/test_address_book.py
# python -m unittest discover -s tests