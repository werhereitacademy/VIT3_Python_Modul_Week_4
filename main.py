# main.py

import book_transactions
import member_transactions

def main():
    print("Welcome to the Library Management System!")
    while True:
        print("\nMenu:")
        print("1. Book Transactions")
        print("2. Member Transactions")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_transactions.book_menu()
        elif choice == "2":
            member_transactions.member_menu()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    main()
