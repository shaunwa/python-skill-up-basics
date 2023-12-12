import os

# This program is nicely separated into functions, which makes it easier to manage
def display_menu():
    print("\n--- Journal Management ---")
    print("1. List Entries")
    print("2. Create New Entry")
    print("3. View Entry")
    print("4. Delete Entry")
    print("5. Exit")
    choice = input("Enter your choice: ")
    return choice

def list_entries():
    with open("journal.txt", "r") as f:
        lines = f.readlines()
        if not lines:
            print("No entries found.")
            return

        print("\n--- All Entries ---")

        for index, line in enumerate(lines):
            print(f"{index + 1}. {line.strip()}")

def create_entry():
    entry = input("Enter your journal entry text: ")
    with open("journal.txt", "a") as f:
        f.write(entry + "\n")
    print("Entry added successfully.\n")

def view_entry():
    list_entries()
    try:
        entry_num = int(input("Enter the number of the entry to view: "))
        with open("journal.txt", "r") as f:
            lines = f.readlines()
            if 0 < entry_num <= len(lines):
                print("\n--- Entry ---")
                print(lines[entry_num - 1].strip())
            else:
                print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def delete_entry():
    list_entries()
    try:
        entry_num = int(input("Enter the number of the entry to delete: "))
        with open("journal.txt", "r") as f:
            lines = f.readlines()
        if 0 < entry_num <= len(lines):
            del lines[entry_num - 1]
            with open("journal.txt", "w") as f:
                f.writelines(lines)
            print("Entry deleted successfully.")
        else:
            print("Invalid entry number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if not os.path.exists("journal.txt"):
    with open("journal.txt", "w") as f:
        pass  # Create an empty file if it doesn't exist

while True:
    choice = display_menu()
    if choice == "1":
        list_entries()
    elif choice == "2":
        create_entry()
    elif choice == "3":
        view_entry()
    elif choice == "4":
        delete_entry()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose from 1 to 5.")