import main


def splash_screen():
    print(
        '-' * 59, '\n' +
        '-', ' ' * 14, 'WELCOME TO PUBLIC LIBRARY', ' ' * 14, '-\n'
                                                              '-', ' ' * 55, '-\n'
                                                                             '-', ' ' * 4, '-> LIST BOOKS    1',
        ' ' * 31, '-\n'
                  '-', ' ' * 4, '-> ADD BOOK      2', ' ' * 31, '-\n'
                                                                '-', ' ' * 4, '-> SEARCH BOOK   3', ' ' * 6,
        '-> BACK           9', ' ' * 4, '-\n'
                                        '-', ' ' * 4, '-> REMOVE BOOK   4', ' ' * 6, '-> EXIT           0', ' ' * 4,
        '-\n'
        '-', ' ' * 55, '-\n' +
        '-' * 59)
    return input()


def book_info(file_path, data=''):
    result = None
    if main.check_file(file_path):
        booklist = main.read_from_json(file_path)
        for book in booklist:
            if data.isnumeric() and int(data) == book['Barkod']:
                result = True, book
                break
            elif data.isalpha() and data.lower() in book['Kitap_Adi'].lower():
                result = True, book
                break
            elif data == '':
                result = False, booklist
                break
            else:
                result = False, 'No book matched with your search!'
        return result
    else:
        result = False, 'Books data file doesn\'t exist!!!'
        return result


def add_book(file_path):
    booklist = []
    barcode = int(input('Enter Barkod: '))
    book_name = input('Enter Book Name: ')
    publisher = input('Enter Publisher: ')
    writer = input('Enter Writer:')
    if main.check_file(file_path):
        booklist = main.read_from_json(file_path)   # Fetch list from the file
    a_book = {
        'Barkod': barcode,
        'Kitap_Adi': book_name,
        'Yayinevi': publisher,
        'Yazar': writer
    }
    booklist.append(a_book)
    main.write_to_json(file_path, booklist)
    return a_book


def search_book(file_path, data=''):
    result = False, 'No book matched with your search!' #result = None
    searched_books = []
    if main.check_file(file_path):
        booklist = main.read_from_json(file_path)
        for book in booklist:
            if data.isnumeric() and int(data) == book['Barkod']:
                searched_books += [book]
                result = True, searched_books
            elif data.isalpha() and data.lower() in book['Kitap_Adi'].lower():
                searched_books += [book]
                result = True, searched_books
            elif data == '':
                print('You didn\'t add any search criteria for your search!!! '
                      'Because of that, you will get all book list...\n')
                result = False, booklist
            # else:
            #     result = False, 'No book matched with your search!'
    else:
        result = False, 'Books data file doesn\'t exist!!!'
    return result
    # if main.check_file(file_path):
    #     booklist = main.read_from_json(file_path)   # Fetch list from the file
    #     if barcode != -1:
    #         for book in booklist:
    #             if book['Barkod'] == barcode:
    #                 for i in range(len(book)):
    #                     print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
    #     else:
    #         print('No book matched with your search!')

    #     if bookname != '':
    #         for book in booklist:
    #             if bookname in book['Kitap_Adi'].lower():
    #                 for i in range(len(book)):
    #                     print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
    #                 print('\n')
    #     else:
    #         print('No book matched with your search!')
    # else:
    #     print('Books data file doesn\'t exist!!!')


def remove_book(file_path, data=''): #remove_book(booklist, barcode=-1, bookname=''):
    if main.check_file(file_path):
        booklist = main.read_from_json(file_path)
        for book1 in booklist:
            if data.isnumeric() and int(data) == book1['Barkod']:
                booklist.remove(book1)
                main.write_to_json(file_path, booklist)
                return True, book1

            # BURASI BIR TURLU CALISMADI, SEBEP BULUNAMADI
            # elif data.isalpha() and data.lower() == book1['Kitap_Adi'].lower():
            #     booklist.remove(book1)
            #     main.write_to_json(file_path, booklist)
            #     return True, book1
    else:
        return False, 'Books data file doesn\'t exist!!!'
    # ESKI REMOVE KODLARI
    # if barcode != -1:
    #     for book in booklist:
    #         if book['Barkod'] == barcode:
    #             booklist.remove(book)
    #             return booklist, book
    #     else:
    #         print('There is no book registered with this "Barcode Number" in the library')
    # elif bookname != '':
    #     for book in booklist:
    #         if bookname in book['Kitap_Adi'].lower():
    #             booklist.remove(book)
    #             return booklist, book
    #     else:
    #         print('There is no book registered with this "Book Name" in the library')


if __name__ == '__main__':
    activity = -1
    book_file_path = 'kitap.json'

    while activity != 9:
        activity = splash_screen()

        # List all books information
        if activity == '1':
            result, book_list = book_info(book_file_path)  # Fetch list from the file
            for book in book_list:
                for i in range(len(book)):
                    print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
                print('\n')  # Send the list for listing process
            input('Press an any key to continue...')

        # Add a new book to the library
        elif activity == '2':
            print('New book adding\n'
                  '---------------\n')
            the_book = add_book(book_file_path)  # New book adding process
            if dict == type(the_book):
                print(f'New book is successfully added. Book name is: {the_book['Kitap_Adi']}\n')
            input('Press an any key to continue...')

        # Search a book in the library
        elif activity == '3':
            searched_book = input('Which book you want to see details?\n'
                                  'Hint: Enter a part of the book name or correct Barcode number:  \n')
            result, searched_book = search_book(book_file_path, searched_book)
            if result:
                if len(searched_book) != 1:
                    print('Multiple results for your search!!!\n'
                          '-----------------------------------')
                for book in searched_book:
                    for i in range(len(book)):
                        print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
                    print('\n')
            input('Press an any key to continue...')

        # Remove a book from library
        elif activity == '4':
            deleted_book = input('Which book you want to see details?\n'
                                 'Hint: Enter correct and full name of book or correct Barcode number:  \n')
            result, deleted_book = remove_book(book_file_path, deleted_book)
            if result:
                print('The book is successfully deletedfrom book list.\n'
                      f'Deleted book: {deleted_book['Kitap_Adi']}')
            else:
                print(deleted_book)
            # book_list = main.read_from_json(book_file_path)  # Fetch list from the file
            # decision = input(
            #     'For removing with "Barcode Number" Press 1  OR For removing with "Book Name" Press 2\n:::: ')
            #
            # if decision == '1':  # Removing via "Barcode Number" code
            #     barcode = int(input('Enter the "Barcode Number" of the book that you want to'
            #                         ' remove from library\n::::'))
            #     book_list, deleted = remove_book(book_list, barcode=barcode)
            #     main.write_to_json(book_file_path, book_list)
            #     print('Deleted book is :\n', deleted)
            #
            # elif decision == '2':  # Removing via "Book Name" code
            #     name = input('Enter the "Book Name" of the book that you want to'
            #                  ' remove from library\n::::').lower()
            #     book_list, deleted = remove_book(book_list, bookname=name)
            #     des2 = input(f'Book to delete:\n{deleted}\n Are you sure to delete? Press Y/N? : ')
            #     if des2.lower() == 'y':
            #         main.write_to_json(book_file_path, book_list)
            #         print('Deleted book is :\n', deleted)
            #     else:
            #         print('The relevant book was not deleted...')
            # else:
            #     print('You didn\'t choose any right option!!!')
            # input('Press an any key to continue...')

        # Return back to main screen
        elif activity == '9':
            break

        # Terminate the program directly
        elif activity == '0':
            main.quit_app()

        # Relist the options in the Book Transactions
        else:
            continue
