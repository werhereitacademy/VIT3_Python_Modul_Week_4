import json
import os
import sys

import book_transactions as bt
import user_transactions as ut
import time as tm

book_file_path = 'kitap.json'


def check_file(file_path):  # Checking whether the file exists in the file path
    try:
        if os.path.exists(file_path):
            return True
        else:
            raise FileNotFoundError('There is no file to read!')
    except FileNotFoundError:
        raise


def read_from_json(file_path):
    if check_file(file_path):
        with open(file_path, 'r') as fp:
            a_list = json.load(fp)
            return a_list


def write2json(file_path, a_list):
    with open(file_path, 'w') as fp:
        json.dump(a_list, fp)
    return a_list


def splash_screen():
    print(
        '-' * 59, '\n' +
        '-', ' ' * 14, 'WELCOME TO PUBLIC LIBRARY', ' ' * 14, '-\n'
                                                              '-', ' ' * 55, '-\n'
                                                                             '-', ' ' * 4, '-> USER TRANSACTIONS    1',
        ' ' * 24, '-\n'
                  '-', ' ' * 4, '-> BOOK TRANSACTIONS    2', ' ' * 24, '-\n'
                                                                       '-', ' ' * 4, '-> QUIT                 0',
        ' ' * 24, '-\n'
                  '-', ' ' * 55, '-\n' +
        '-' * 59)
    return input()


def quit_app():
    print('Program is ending!')
    quit()


if __name__ == '__main__':

    while True:
        try:
            activity = splash_screen()
            if activity == '1':
                print('User trans')
            elif activity == '2':
                while activity != 9:
                    activity = bt.splash_screen()

                    # List all books information
                    if activity == '1':
                        book_list = read_from_json(book_file_path)  # Fetch list from the file
                        bt.book_info(book_list)  # Send the list for listing process
                        input('Press an any key to continue...')

                    # Add a new book to the library
                    elif activity == '2':
                        book_list = read_from_json(book_file_path)  # Fetch list from the file
                        book_list = bt.add_book(book_file_path, book_list)  # Send the list for adding process
                        write2json(book_file_path, book_list)  # Write the updated list to the file
                        input('Press an any key to continue...')

                    # Search a book in the library
                    elif activity == '3':
                        book_list = read_from_json(book_file_path)  # Fetch list from the file
                        decision = input(
                            'For searching with "Barcode Number" Press 1  OR For searching with "Book Name" Press 2\n:::: ')
                        if decision == '1':
                            barcode = int(
                                input('Enter the "Barcode Number" that you want to see details of the book: '))
                            bt.search_book(book_list, barcode=barcode)
                        elif decision == '2':
                            name = input('Enter the "Book Name" that you want to see details of the book: ').lower()
                            bt.search_book(book_list, bookname=name)
                        else:
                            print('You didn\'t choose any right option!!!')
                        input('Press an any key to continue...')

                    # Remove a book from library
                    elif activity == '4':
                        book_list = read_from_json(book_file_path)  # Fetch list from the file
                        decision = input(
                            'For removing with "Barcode Number" Press 1  OR For removing with "Book Name" Press 2\n:::: ')

                        if decision == '1':  # Removing via "Barcode Number" code
                            barcode = int(input('Enter the "Barcode Number" of the book that you want to'
                                                ' remove from library\n::::'))
                            book_list, deleted = bt.remove_book(book_list, barcode=barcode)
                            write2json(book_file_path, book_list)
                            print('Deleted book is :\n', deleted)

                        elif decision == '2':  # Removing via "Book Name" code
                            name = input('Enter the "Book Name" of the book that you want to'
                                         ' remove from library\n::::').lower()
                            book_list, deleted = bt.remove_book(book_list, bookname=name)
                            des2 = input(f'Book to delete:\n{deleted}\n Are you sure to delete? Press Y/N? : ')
                            if des2.lower() == 'y':
                                write2json(book_file_path, book_list)
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
                        quit_app()

                    # Relist the options in the Book Transactions
                    else:
                        continue

            # Terminate the program directly
            elif activity == '0':
                quit_app()

            # Relist the options in the Main Screen
            else:
                continue

        except Exception as e:
            print('ERROR: ', sys.exc_info()[0], ': ', e)
