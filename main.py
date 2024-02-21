import json
import os
import sys

import book_transactions as bt
import user_transactions as ut


def check_file(file_path):  # Checking whether the file exists in the file path
    try:
        if os.path.exists(file_path):
            return True
        else:
            return False
            #   raise FileNotFoundError('There is no file to read!')
    except FileNotFoundError:
        raise


def read_from_json(file_path):
    if check_file(file_path):
        with open(file_path, 'r', encoding='UTF-8') as fp:
            a_list = json.load(fp)
            return a_list


def write_to_json(file_path, a_list):
    with open(file_path, 'w', encoding='UTF-8') as fp:
        json.dump(a_list, fp, indent=4)
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
    activity = -1
    book_file_path = 'kitap.json'
    user_file_path = 'users.json'
    follow_file_path = 'follow.json'

    while True:
        try:
            activity = splash_screen()
            if activity == '1':

                while activity != 9:
                    activity = ut.splash_screen()

                    # List all users information
                    if activity == '1':
                        print('Listing all users\n'
                              '---------------------\n')
                        # Call the list_users function
                        result, user_list = ut.list_users(user_file_path)
                        if not result:  # list_user function returns True or False bool value ;)
                            print(user_list)
                        input('Press the Enter key to continue...')

                    # Add a new user to the library system
                    elif activity == '2':
                        print('Adding a new user to library\n'
                              '----------------------------\n')
                        full_name = input('Enter user full name: ')
                        phone = input('Enter user phone number: ')
                        address = input('Enter user adress: ')

                        # Call add_user function and get back added user information to the added_user variable
                        added_user = ut.add_user(user_file_path)

                        if dict == type(added_user):
                            print(f'The user is added successfully as:\n'
                                  f'Full Name ==> {added_user['full_name']}\n'
                                  f'Phone     ==> {added_user['phone']}\n'
                                  f'Address   ==> {added_user['address']}\n'
                                  )
                        else:
                            print('The adding process is unsuccessful or wrong type adding!')
                        input('Press the Enter key to continue...')

                    # Update a user information in the library system
                    elif activity == '3':
                        print('Updating a user in the library user list\n'
                              '----------------------------------------\n')
                        if check_file(user_file_path):
                            the_user = input('Type the name of the user you want to update: ')
                            the_user_list = ut.search_user(user_file_path, the_user)

                            if len(the_user_list) >= 1:
                                if len(the_user_list) > 1:  # Adding extra info, if there are more results
                                    print('There are multiple results based on your search criteria! Like this:\n')
                                for the_user in the_user_list:
                                    print(f'ID: {the_user['id']}\n'
                                          f'{the_user['full_name']}\n'
                                          f'{the_user['phone']}\n'
                                          f'{the_user['address']}\n\n'
                                          )
                                the_id = int(input("Enter the ID number of the user you want to update:"))

                                # Call user_update function and get updated information back to the updated_user variable
                                result, updated_user = ut.update_user(user_file_path, the_id)

                                if result:
                                    print(f'The user is updated as:\n'
                                          f'==> {updated_user['full_name']}\n'
                                          f'==> {updated_user['phone']}\n'
                                          f'==> {updated_user['address']}\n'
                                          )
                                else:
                                    print('The user doesn\'t exist that you want to update!')
                            else:
                                print('No user matched with your search!')
                        else:
                            print('Users data file doesn\'t exist!!!')
                        input('Press the Enter key to continue...')

                    # Search a user in the library system
                    elif activity == '4':
                        print('Searching a user in the library user list\n'
                              '-----------------------------------------\n')
                        if check_file(user_file_path):
                            the_user_name = input('Type the name of the user you want to get information about him/her: ')
                            result, the_user_list = ut.search_user(user_file_path, the_user_name)
                            if result:
                                print('Found user(s) information:\n'
                                      '--------------------------\n')
                                for the_user in the_user_list:
                                    print(f'ID:             {the_user['id']}\n'
                                          f'Name-Surname:   {the_user['full_name']}\n'
                                          f'Phone Number:   {the_user['phone']}\n'
                                          f'Address:        {the_user['address']}\n\n'
                                          )
                            else:
                                print(the_user_list)
                        else:
                            print('The users\' data file doesn\'t exist!!!\n')
                        input('Press the Enter key to continue...')

                    # Delete a user from the library system
                    elif activity == '5':
                        print('Removing a user from the library user list\n'
                              '------------------------------------------\n')
                        if check_file(user_file_path):
                            the_user = input('Type the name of the user you want to delete: ')
                            the_user_list = ut.search_user(user_file_path, the_user)[1]
                            print(type(the_user_list))

                            if len(the_user_list) >= 1 and type(the_user_list) == list:
                                if len(the_user_list) > 1:  # Adding extra info, if there are more results
                                    print('There are multiple results based on your search criteria! Here you are:\n')
                                for the_user in the_user_list:
                                    print(f'ID: {the_user['id']}\n'
                                          f'{the_user['full_name']}\n'
                                          f'{the_user['phone']}\n'
                                          f'{the_user['address']}\n\n'
                                          )
                                the_id = int(input("Enter the ID number of the user you want to delete:"))

                                # Call user_delete function and get updated information back to the deleted_user variable
                                result, deleted_user = ut.delete_user(user_file_path, the_id)

                                if result:
                                    print(f'The user; {deleted_user['full_name']} is successfully deleted from the user list!')
                                else:
                                    print('The user doesn\'t exist that you want to delete!')
                            else:
                                print('No user matched with your search!')
                        else:
                            print('Users data file doesn\'t exist!!!')
                        input('Press the Enter key to continue...')

                    # Lending a book to a user
                    elif activity == '6':
                        print('Lending a book to a user\n'
                              '------------------------\n')
                        lent_book = input('Which book you want to lend?: ')
                        result, lent_book = bt.book_info(book_file_path, lent_book)
                        if result:
                            if len(lent_book) == 4 or len(lent_book) == 6:
                                print(f'The book is {lent_book['Kitap_Adi']}')
                            else:  # len(lent_book) > 1:
                                print('Too many book is chosen, please retype book info:')
                                break
                        else:
                            print(lent_book)

                        # the book has just been chosen, now choose the user! #

                        lend2user = input('To which user will you lend this book? Enter user name or id: ')
                        result, lend2user = ut.search_user(user_file_path, lend2user)
                        if result:
                            if len(lend2user) == 1:
                                print(f'The user is {lend2user[0]['full_name']}')
                                result, lent_process_dict = ut.lend_book(follow_file_path, lent_book, lend2user)
                                if result:
                                    print(f'"{lent_process_dict['book']['Kitap_Adi']}" is registered to '
                                          f'"{lent_process_dict['user']['full_name']}" at {lent_process_dict['lend_date']}\n'
                                          f'The book return date: {lent_process_dict['return_date']}')
                            else:
                                print('Too many user is chosen, please retype user info again:')
                                break
                        else:
                            print(lend2user + ' Restart lending process...\n')

                    # Returning a book
                    elif activity == '7':
                        print('Returning a book from a user\n'
                              '------------------------\n')
                        print('It is still under coding...')

                    # Tracking the books
                    elif activity == '8':
                        print('Tracking the books\n'
                              '------------------\n')
                        print('It is still under coding...')

                    # Return back to main screen
                    elif activity == '9':
                        break

                    # Terminate the program directly
                    elif activity == '0':
                        quit_app()

                    # Relist the options in the Book Transactions
                    else:
                        continue

            elif activity == '2':
                while activity != 9:
                    activity = bt.splash_screen()

                    # List all books information
                    if activity == '1':
                        result, book_list = bt.book_info(book_file_path)  # Fetch list from the file
                        for book in book_list:
                            for i in range(len(book)):
                                print(f'{list(book.items())[i][0]}= {list(book.items())[i][1]}')
                            print('\n')  # Send the list for listing process
                        input('Press an any key to continue...')

                    # Add a new book to the library
                    elif activity == '2':
                        print('New book adding\n'
                              '---------------\n')
                        the_book = bt.add_book(book_file_path)  # New book adding process
                        if dict == type(the_book):
                            print(f'New book is successfully added. Book name is: {the_book['Kitap_Adi']}\n')
                        input('Press an any key to continue...')

                    # Search a book in the library
                    elif activity == '3':
                        searched_book = input('Which book you want to see details?\n'
                                              'Hint: Enter a part of the book name or correct Barcode number:  \n')
                        result, searched_book = bt.search_book(book_file_path, searched_book)
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
                        result, deleted_book = bt.remove_book(book_file_path, deleted_book)
                        if result:
                            print('The book is successfully deletedfrom book list.\n'
                                  f'Deleted book: {deleted_book['Kitap_Adi']}')
                        else:
                            print(deleted_book)

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
