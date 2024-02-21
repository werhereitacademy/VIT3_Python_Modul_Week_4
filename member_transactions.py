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

# Define other member functions: delete_member, search_member, update_member, member_menu, etc.
