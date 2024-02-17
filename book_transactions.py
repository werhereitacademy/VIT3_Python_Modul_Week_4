import main


def splash_screen():
    print(
        '-' * 59, '\n' +
        '-', ' ' * 14, 'WELCOME TO PUBLIC LIBRARY', ' ' * 14, '-\n'
        '-', ' ' * 55, '-\n'
        '-', ' ' * 4, '-> LIST BOOKS    1', ' ' * 31, '-\n'
        '-', ' ' * 4, '-> ADD BOOK      2', ' ' * 31, '-\n'
        '-', ' ' * 4, '-> SEARCH BOOK   3', ' ' * 6, '-> BACK           9', ' ' * 4, '-\n'
        '-', ' ' * 4, '-> REMOVE BOOK   4', ' ' * 6, '-> EXIT           0', ' ' * 4, '-\n'
        '-', ' ' * 55, '-\n' +
        '-' * 59)
    return input()


def book_info(booklist):
    for book in booklist:
        for i in range(len(book)):
            print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
        print('\n')


def add_book(file_path, booklist):
    print('New book adding...:')
    barcode = int(input('Enter Barkod: '))
    book_name = input('Enter Book Name: ')
    publisher = input('Enter Publisher: ')
    writer = input('Enter Writer:')
    a_book = {
        'Barkod': barcode,
        'Kitap_Adi': book_name,
        'Yayinevi': publisher,
        'Yazar': writer
    }
    booklist.append(a_book)
    return booklist


def search_book(booklist, barcode= -1, bookname= ''):
    if barcode != -1:
        for book in booklist:
            if book['Barkod'] == barcode:
                for i in range(len(book)):
                    print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
            else:
                print('There is no book registered with this "Barcode Number" in the library')
    elif bookname != '':
        for book in booklist:
            if bookname in book['Kitap_Adi'].lower():
                for i in range(len(book)):
                    print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
                print('\n')
                #break
        else:
            print('There is no book registered with this "Book Name" in the library')


def remove_book(booklist, barcode= -1, bookname= ''):
    if barcode != -1:
        for book in booklist:
            if book['Barkod'] == barcode:
                booklist.remove(book)
                return booklist, book
        else:
            print('There is no book registered with this "Barcode Number" in the library')
    elif bookname != '':
        for book in booklist:
            if bookname in book['Kitap_Adi'].lower():
                booklist.remove(book)
                return booklist, book
        else:
            print('There is no book registered with this "Book Name" in the library')


if __name__ == '__main__':
    activity = -1
    book_file_path = 'kitap.json'

    while activity != 9:
        activity = splash_screen()

        # List all books information
        if activity == '1':
            book_list = main.read_from_json(book_file_path)  # Fetch list from the file
            book_info(book_list)  # Send the list for listing process
            input('Press an any key to continue...')

        # Add a new book to the library
        elif activity == '2':
            book_list = main.read_from_json(book_file_path)  # Fetch list from the file
            book_list = add_book(book_file_path, book_list)  # Send the list for adding process
            main.write_to_json(book_file_path, book_list)  # Write the updated list to the file
            input('Press an any key to continue...')

        # Search a book in the library
        elif activity == '3':
            book_list = main.read_from_json(book_file_path)  # Fetch list from the file
            decision = input(
                'For searching with "Barcode Number" Press 1  OR For searching with "Book Name" Press 2\n:::: ')
            if decision == '1':
                barcode = int(
                    input('Enter the "Barcode Number" that you want to see details of the book: '))
                search_book(book_list, barcode=barcode)
            elif decision == '2':
                name = input('Enter the "Book Name" that you want to see details of the book: ').lower()
                search_book(book_list, bookname=name)
            else:
                print('You didn\'t choose any right option!!!')
            input('Press an any key to continue...')

        # Remove a book from library
        elif activity == '4':
            book_list = main.read_from_json(book_file_path)  # Fetch list from the file
            decision = input(
                'For removing with "Barcode Number" Press 1  OR For removing with "Book Name" Press 2\n:::: ')

            if decision == '1':  # Removing via "Barcode Number" code
                barcode = int(input('Enter the "Barcode Number" of the book that you want to'
                                    ' remove from library\n::::'))
                book_list, deleted = remove_book(book_list, barcode=barcode)
                main.write_to_json(book_file_path, book_list)
                print('Deleted book is :\n', deleted)

            elif decision == '2':  # Removing via "Book Name" code
                name = input('Enter the "Book Name" of the book that you want to'
                             ' remove from library\n::::').lower()
                book_list, deleted = remove_book(book_list, bookname=name)
                des2 = input(f'Book to delete:\n{deleted}\n Are you sure to delete? Press Y/N? : ')
                if des2.lower() == 'y':
                    main.write_to_json(book_file_path, book_list)
                    print('Deleted book is :\n', deleted)
                else:
                    print('The relevant book was not deleted...')
            else:
                print('You didn\'t choose any right option!!!')
            input('Press an any key to continue...')

        # Return back to main screen
        elif activity == '9':
            break

        # Terminate the program directly
        elif activity == '0':
            main.quit_app()

        # Relist the options in the Book Transactions
        else:
            continue
