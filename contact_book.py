import json
import os

contacts = []

# Load contacts from file if exists
def load_contacts():
    global contacts
    if os.path.exists("contacts.json"):
        with open("contacts.json", "r") as f:
            contacts = json.load(f)

# Save contacts to file (sorted by name)
def save_contacts():
    sorted_contacts = sorted(contacts, key=lambda x: x['name'].lower())
    with open("contacts.json", "w") as f:
        json.dump(sorted_contacts, f, indent=4)

# Add contact (phone must be 10 digits)
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone (10 digits): ").strip()
    
    if not phone.isdigit() or len(phone) != 10:
        print("❌ Phone number must be exactly 10 digits.")
        return
    
    contacts.append({"name": name, "phone": phone})
    save_contacts()
    print("✅ Contact added successfully!")

# View contacts
def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
        return
    print("\n📒 Contact List:")
    print("-" * 40)
    for c in sorted(contacts, key=lambda x: x['name'].lower()):
        print(f"Name: {c['name']}, Phone: {c['phone']}")
    print("-" * 40)

# Search contact by name or phone
def search_contact():
    query = input("Enter name or phone to search: ").strip().lower()
    results = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    
    print("\n🔍 Search Results:")
    print("-" * 40)
    if results:
        for c in results:
            print(f"Name: {c['name']}, Phone: {c['phone']}")
    else:
        print("❌ No contact found with that detail.")
    print("-" * 40)

# Update contact (search by name)
def update_contact():
    name = input("Enter the name of the contact to update: ").strip().lower()
    for c in contacts:
        if c['name'].lower() == name:
            new_name = input(f"Enter new name (Leave blank to keep '{c['name']}'): ").strip()
            new_phone = input(f"Enter new phone (10 digits, leave blank to keep '{c['phone']}'): ").strip()
            
            if new_name:
                c['name'] = new_name
            if new_phone:
                if not new_phone.isdigit() or len(new_phone) != 10:
                    print("❌ Phone number must be exactly 10 digits.")
                    return
                c['phone'] = new_phone
            
            save_contacts()
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

# Delete contact (search by name)
def delete_contact():
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for c in contacts:
        if c['name'].lower() == name:
            contacts.remove(c)
            save_contacts()
            print("✅ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

# Main menu
def main():
    load_contacts()
    while True:
        print("\n===== 📞 Contact Book Menu =====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid option, please try again.")

if __name__ == "__main__":
    main()
