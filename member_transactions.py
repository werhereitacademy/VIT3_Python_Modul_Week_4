# member_transactions.py

import json
import os

MEMBERS_FILE = "members.json"

def load_members():
    if not os.path.exists(MEMBERS_FILE):
        with open(MEMBERS_FILE, "w") as f:
            json.dump([], f)
    with open(MEMBERS_FILE, "r") as f:
        return json.load(f)

def save_members(members):
    with open(MEMBERS_FILE, "w") as f:
        json.dump(members, f, indent=4)

def add_member():
    members = load_members()
    id = input("Enter the ID: ")
    member_name = input("Enter the member name: ")
    tel = input("Enter the telephone number: ")
    address = input("Enter the address: ")

    new_member = {
        "id": id,
        "member_name": member_name,
        "tel": tel,
        "address": address
    }
    members.append(new_member)
    save_members(members)
    print("Member added successfully.")

def delete_member():
    members = load_members()
    id = input("Enter the ID of the member to delete: ")

    for member in members:
        if member["id"] == id:
            members.remove(member)
            save_members(members)
            print("Member deleted successfully.")
            return

    print("Member not found.")

def search_member():
    members = load_members()
    id = input("Enter the ID of the member to search: ")

    for member in members:
        if member["id"] == id:
            print("Member found:")
            print(member)
            return

    print("Member not found.")

def update_member():
    members = load_members()
    id = input("Enter the ID of the member to update: ")

    for member in members:
        if member["id"] == id:
            print("Enter new information (leave blank to keep unchanged):")
            member_name = input("Enter the new member name: ")
            if member_name:
                member["member_name"] = member_name
            tel = input("Enter the new telephone number: ")
            if tel:
                member["tel"] = tel
            address = input("Enter the new address: ")
            if address:
                member["address"] = address

            save_members(members)
            print("Member updated successfully.")
            return

    print("Member not found.")

def member_menu():
    while True:
        print("\nMember Transactions Menu:")
        print("1. Add Member")
        print("2. Delete Member")
        print("3. Search Member")
        print("4. Update Member")
        print("5. Return to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_member()
        elif choice == "2":
            delete_member()
        elif choice == "3":
            search_member()
        elif choice == "4":
            update_member()
        elif choice == "5":
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
