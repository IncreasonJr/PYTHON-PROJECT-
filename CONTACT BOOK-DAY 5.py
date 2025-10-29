contacts = {}

def add_contact(name, number):
    contacts[name] = number
    print(f"Contact {name} added successfully")

def view_contact(name):
    if name in contacts:
        print(f"Name: {name}, Number: {contacts[name]}")
    else:
        print("Contact not found")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully")
    else:
        print("Contact not found")

def view_all_contacts():
    if contacts:
        print("\nAll Contacts:")
        for name, number in contacts.items():
            print(f"Name: {name}, Number: {number}")
    else:
        print("No contacts found")

def main():
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter name: ")
            number = input("Enter number: ")
            add_contact(name, number)
        
        elif choice == '2':
            name = input("Enter name to search: ")
            view_contact(name)
        
        elif choice == '3':
            name = input("Enter name to delete: ")
            delete_contact(name)
        
        elif choice == '4':
            view_all_contacts()
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()