class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                return contact
        return None

    def update_contact(self, name, phone, email):
        contact = self.search_contact(name)
        if contact:
            contact.phone = phone
            contact.email = email
            print(f"Contact '{name}' updated.")
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        contact = self.search_contact(name)
        if contact:
            self.contacts.remove(contact)
            print(f"Contact '{name}' deleted.")
        else:
            print(f"Contact '{name}' not found.")

    def display_contacts(self):
        print("Contact Book:")
        for contact in self.contacts:
            print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n")

    def display_by_alphabet(self, alphabet):
        print(f"Contacts starting with '{alphabet}':")
        for contact in self.contacts:
            if contact.name.lower().startswith(alphabet.lower()):
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n")

def main():
    contact_book = ContactBook()

    while True:
        print("\n1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display All Contacts")
        print("6. Display Contacts by Alphabet")
        print("7. Exit")

        choice = int(input("Select an option: "))

        if choice == 1:
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            contact = Contact(name, phone, email)
            contact_book.add_contact(contact)
            print("Contact added.")
        elif choice == 2:
            name = input("Enter name to search: ")
            contact = contact_book.search_contact(name)
            if contact:
                print(f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\n")
            else:
                print(f"Contact '{name}' not found.")
        elif choice == 3:
            name = input("Enter name to update: ")
            phone = input("New phone: ")
            email = input("New email: ")
            contact_book.update_contact(name, phone, email)
        elif choice == 4:
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)
        elif choice == 5:
            contact_book.display_contacts()
        elif choice == 6:
            alphabet = input("Enter an alphabet: ")
            contact_book.display_by_alphabet(alphabet)
        elif choice == 7:
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
