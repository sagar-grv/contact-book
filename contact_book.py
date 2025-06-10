import os

# File to store contact data
FILE_NAME = "contacts.txt"

# Dictionary to hold all contacts in memory
contacts = {}

# Load contacts from file at the start
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
    else:
        # Create file if not exists
        open(FILE_NAME, "w").close()

# Save contacts to file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")

# Add a new contact
def add_contact():
    name = input("Enter name: ").strip()
    if name in contacts:
        print("❗ Contact already exists.")
        return
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    contacts[name] = {"phone": phone, "email": email}
    save_contacts()
    print("✅ Contact added.")

# View all contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
    else:
        print("\n--- All Contacts ---")
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Search for a contact
def search_contact():
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"✅ Found: {name} - Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("❌ Contact not found.")

# Delete a contact
def delete_contact():
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts()
        print("🗑️ Contact deleted.")
    else:
        print("❌ Contact not found.")

# Menu loop
def menu():
    while True:
        print("\n📇 Welcome to the Contact Book!\n Created By Sagar Gurav In BTech 1st Year")
        print("\n📇 Contact Book Menu:")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

# Start the program
if __name__ == "__main__":
    load_contacts()
    menu()
