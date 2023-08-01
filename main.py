class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, details):
        self.contacts[name] = details
        print(f"Contact '{name}' added successfully!")

    def search_contact(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return None

    def update_contact(self, name, details):
        if name in self.contacts:
            self.contacts[name] = details
            print(f"Contact '{name}' updated successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print(f"Contact '{name}' not found!")

    def display_contact_book(self):
        if self.contacts:
            print("Contact Book:")
            for name, details in self.contacts.items():
                print(f"{name}: {details}")
        else:
            print("Contact book is empty!")

    def display_contacts_with_alphabet(self, alphabet):
        matching_contacts = {name: details for name, details in self.contacts.items() if name.startswith(alphabet)}
        if matching_contacts:
            print(f"Contacts with the alphabet '{alphabet}':")
            for name, details in matching_contacts.items():
                print(f"{name}: {details}")
        else:
            print(f"No contacts found with the alphabet '{alphabet}'.")


def main():
    contact_book = ContactBook()

    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add new contact")
        print("2. Search for a person")
        print("3. Update existing contact")
        print("4. Delete existing contact")
        print("5. Display all contacts")
        print("6. Display contacts with specific alphabet")
        print("7. Exit")

        choice = int(input("Enter your choice (1-7): "))

        if choice == 1:
            name = input("Enter the name: ")
            details = input("Enter the details: ")
            contact_book.add_contact(name, details)

        elif choice == 2:
            name = input("Enter the name to search: ")
            result = contact_book.search_contact(name)
            if result:
                print(f"Contact Details:\n{name}: {result}")
            else:
                print(f"Contact '{name}' not found!")

        elif choice == 3:
            name = input("Enter the name to update: ")
            details = input("Enter the new details: ")
            contact_book.update_contact(name, details)

        elif choice == 4:
            name = input("Enter the name to delete: ")
            contact_book.delete_contact(name)

        elif choice == 5:
            contact_book.display_contact_book()

        elif choice == 6:
            alphabet = input("Enter the alphabet: ")
            contact_book.display_contacts_with_alphabet(alphabet)

        elif choice == 7:
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please choose again.")


if __name__ == "__main__":
    main()
