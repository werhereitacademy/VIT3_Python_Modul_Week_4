import json
import os

def read():
    with open("book.json", "r", encoding="utf-8") as file:
        books = json.load(file)
    return books

def record(books):
    with open('book.json', 'w') as file:
        json.dump(books, file)
        print("Your data has been updated.")

def add_book():
    new_book_name = input("Please enter the name of the new book:")
    new_book_author = input("Please enter the author of the new book:")
    new_book_publisher = input("Please enter the publisher of the new book:")
    new_book_barcode = input("Please enter the barcode number of the new book:")
    new_book_language = input("Please enter the language of the new book:")
    new_book = {"Barkod": new_book_barcode, "Dil": new_book_language, "Kitap_Adi": new_book_name,
                "Yayinevi": new_book_publisher, "Yazar": new_book_author}
    books = read()
    books.append(new_book)
    record(books)

def delete_book():
    book_to_delete = input("Please enter the name of the book you want to delete:")
    books = read()
    new_books = [book for book in books if book["Kitap_Adi"].lower() != book_to_delete.lower()]
    with open("book.json", "w") as file:
        json.dump(new_books, file)

def search_book():
    books = read()
    search_book_title = input("Please enter the book you want to search:")
    search_book_title = search_book_title.lower()
    found_books = []
    for book in books:
        if search_book_title in book["Kitap_Adi"].lower():
            found_books.append(book)
    if len(found_books) >= 1:
        print("Found books:")
        for found_book in found_books:
            print(found_book)
    else:
        print("No books found with the entered book title.")

def view_books():
    choice = input("To see the books in our library, press `1`\nTo go back, press `0`:")
    books = read()
    n = 1
    if choice == "1":
        for book in books:
            print(f"{n}.{book['Kitap_Adi']}")
            n += 1
    elif choice == "0":
        return

if __name__ == "__main__":
    print("Operation")
