import main
import book_transactions as bt
import library_time as tm


def splash_screen():
    print(
        '-' * 59, '\n' +
        '-', ' ' * 18, 'BOOK TRANSACTIONS', ' ' * 18, '-\n'
                                                      '-', ' ' * 55, '-\n'
                                                                     '-', ' ' * 4, '-> LIST USERS    1', ' ' * 6,
        '-> LEND BOOK      6', ' ' * 4, '-\n'
                                        '-', ' ' * 4, '-> ADD USER      2', ' ' * 6, '-> RETURN BOOK    7', ' ' * 4,
        '-\n'
        '-', ' ' * 4, '-> UPDATE USER   3', ' ' * 6, '-> TRACK BOOK     8', ' ' * 4, '-\n'
                                                                                     '-', ' ' * 4, '-> SEARCH USER   4',
        ' ' * 6, '-> BACK           9', ' ' * 4, '-\n'
                                                 '-', ' ' * 4, '-> REMOVE USER   5', ' ' * 6, '-> EXIT           0',
        ' ' * 4, '-\n'
                 '-', ' ' * 55, '-\n' +
        '-' * 59)
    return input()


def list_users(file_path):
    if main.check_file(file_path):
        userlist = main.read_from_json(file_path)
        for user in userlist:
            print(f'ID:             {user['id']}\n'
                  f'Name-Surname:   {user['full_name']}\n'
                  f'Phone Number:   {user['phone']}\n'
                  f'Address:        {user['address']}\n\n'
                  )
        return True, userlist
    else:
        return False, 'Users data file doesn\'t exist!!!'


def add_user(file_path):
    if main.check_file(file_path):
        userlist = main.read_from_json(file_path)
        if len(userlist) == 0:
            id_ = 0
        else:
            id_ = userlist[-1]['id']
        a_user = {'id': id_ + 1,
                  'full_name': full_name,
                  'phone': phone,
                  'address': address
                  }
    else:
        userlist = []
        a_user = {'id': 1,
                  'full_name': full_name,
                  'phone': phone,
                  'address': address
                  }
    userlist.append(a_user)
    main.write_to_json(file_path, userlist)
    return a_user


def update_user(file_path, id_):
    if main.check_file(file_path):
        userlist = main.read_from_json(file_path)
        for user in userlist:
            if user['id'] == id_:
                n_name = input(f'Enter new name for {user['full_name']}:')
                user['phone'] = input(f'Enter new phone for {user['full_name']}: ')
                user['address'] = input(f'Enter new address for {user['full_name']}: ')
                user['full_name'] = n_name
                main.write_to_json(file_path, userlist)
                result = user
                break
            else:
                result = 'The user doesn\'t exist that you want to update!\n'

        return True, result
    else:
        return False, 'Users data file doesn\'t exist!!!\n'


def search_user(file_path, data=''):
    if main.check_file(file_path):
        userlist = main.read_from_json(file_path)
        n_userlist = []
        for user in userlist:
            if data.isnumeric() and int(data) == user['id']:
                n_userlist += [user]
            elif data.isalpha() and data.lower() in user['full_name'].lower():
                n_userlist += [user]
        if len(n_userlist) != 0:
            return True, n_userlist
        else:
            return False, 'The user doesn\'t exist that you search!'
    else:
        return False, 'Users data file doesn\'t exist!!!'


def delete_user(file_path, id_):
    result = 'Users data file doesn\'t exist!!!'
    if main.check_file(file_path):
        userlist = main.read_from_json(file_path)
        for user in userlist:
            if user['id'] == id_:
                userlist.remove(user)
                main.write_to_json(file_path, userlist)
                result = user
                break
            else:
                # print('The user doesn\'t exist that you want to delete!')
                result = 'The user doesn\'t exist that you want to delete!'
        return True, result
    else:
        return False, result


def lend_book(file_path, book_info, user_info):
    if book_info['Kira_Durumu'] == 0:
        follow_list = []  # Created a list... It will help us if there is no file
        lending_process_dict = {}
        if main.check_file(file_path):  # if there is a file ==>
            follow_list = main.read_from_json(file_path)
            if len(follow_list) == 0:  # if the file is empty
                id_ = 0
            else:  # if there is a value in the file
                id_ = follow_list[-1]['id']
            lending_process_dict['id'] = id_ + 1
        else:  # if there is no file, assign id_ = 1
            lending_process_dict['id'] = 1
        #  Add other key-values to the lending process dictionary
        lending_process_dict['book'] = book_info
        lending_process_dict['user'] = user_info[0]
        lending_process_dict['lend_date'] = tm.return_date1()[0]
        lending_process_dict['return_date'] = tm.return_date1()[1]

        follow_list.append(lending_process_dict)  # Add the new created dictionary to the list

        main.write_to_json(follow_file_path, follow_list)  # Write updated list to the json file

        return True, lending_process_dict  # return a bool value and the new dictionary
    else:
        return False, 'The book has already been lent to another user!'


def return_book(file_path, returnedbook):
    result = 'Follow list data file doesn\'t exist!!!'
    if main.check_file(follow_file_path):
        followlist = main.read_from_json(follow_file_path)
        if len(followlist) > 0:
            for case in followlist:
                if returnedbook.isnumeric() and int(returnedbook) == case['book']['Barkod']:
                    bt.update_book(file_path, case['book']['Barkod'], 0)
                    result = True, case
                    followlist.remove(case)
                    main.write_to_json(follow_file_path, followlist)
                    break
                elif returnedbook.isalpha() and returnedbook.lower() in case['book']['Kitap_Adi'].lower():
                    bt.update_book(file_path, case['book']['Barkod'], 0)
                    result = True, case
                    followlist.remove(case)
                    main.write_to_json(follow_file_path, followlist)
                    break
                else:
                    result = False, 'The book is not in follow list!'
        else:
            result = False, 'The follow list is empty!'
        return result
    else:
        return result


def track_book(file_path):
    if main.check_file(file_path):
        followlist = main.read_from_json(file_path)
        if len(followlist) > 0:
            for case in followlist:
                print(
                    f'The book: {case['book']['Kitap_Adi']} is lent to {case['user']['full_name']} on '
                    f'{case['lend_date'][0:10]} and it must be returned on {case['return_date']}\n\n'
                )
        else:
            print('Result: There is no info for book tracking!\n'
                  'Reason: The follow list is empty!')


if __name__ == '__main__':

    activity = -1
    book_file_path = 'kitap.json'
    user_file_path = 'users.json'
    follow_file_path = 'follow.json'

    while activity != 9:
        try:
            activity = splash_screen()

            # List all users information
            if activity == '1':
                print('Listing all users\n'
                      '---------------------\n')
                # Call the list_users function
                result, user_list = list_users(user_file_path)
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
                added_user = add_user(user_file_path)

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
                if main.check_file(user_file_path):
                    the_user = input('Type the name of the user you want to update: ')
                    the_user_list = search_user(user_file_path, the_user)

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
                        result, updated_user = update_user(user_file_path, the_id)

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
                if main.check_file(user_file_path):
                    the_user_name = input('Type the name of the user you want to get information about him/her: ')
                    result, the_user_list = search_user(user_file_path, the_user_name)
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
                if main.check_file(user_file_path):
                    the_user = input('Type the name of the user you want to delete: ')
                    the_user_list = search_user(user_file_path, the_user)[1]
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
                        result, deleted_user = delete_user(user_file_path, the_id)

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
                    if len(lent_book) == 5 or len(lent_book) == 7:
                        print(f'The book is {lent_book['Kitap_Adi']}')
                    else:  # len(lent_book) > 1:
                        print('Too many book is chosen, please retype book info:')
                        break
                else:
                    print(lent_book)

                # the book has just been chosen, now choose the user! #

                lend2user = input('To which user will you lend this book? Enter user name or id: ')
                result, lend2user = search_user(user_file_path, lend2user)
                if result:
                    if len(lend2user) == 1:
                        print(f'The user is {lend2user[0]['full_name']}')
                        result, lent_process_dict = lend_book(follow_file_path, lent_book, lend2user)
                        if result:
                            result, reason = bt.update_book(book_file_path, lent_process_dict['book']['Barkod'],
                                                            lent_process_dict['user']['id'])
                            if result:
                                print(f'"{lent_process_dict['book']['Kitap_Adi']}" is registered to '
                                      f'"{lent_process_dict['user']['full_name']}" at {lent_process_dict['lend_date']}\n'
                                      f'The book return date: {lent_process_dict['return_date']}')
                            else:
                                print(reason)
                        else:
                            print(lent_process_dict)
                    else:
                        print('Too many user is chosen, please retype user info again:')
                        break
                else:
                    print(lend2user + ' Restart lending process...\n')

            # Returning a book
            elif activity == '7':
                print('Returning a book from a user\n'
                      '----------------------------\n')
                returned_book = input('Enter the "full name of the book" or "barcode number":  ')
                result, returned_book = return_book(book_file_path, returned_book)

                if result:
                    print(f'The book: "{returned_book['book']['Kitap_Adi']}" has successfully been unregistered from '
                          f'the user: "{returned_book['user']['full_name']}"...')
                else:
                    print('Failed:', returned_book)

                input('Press the Enter key to continue...')

            # Tracking the books
            elif activity == '8':
                print('Tracking the books\n'
                      '------------------\n')
                track_book(follow_file_path)
                input('Press the Enter key to continue...')

            # Return back to main screen
            elif activity == '9':
                break

            # Terminate the program directly
            elif activity == '0':
                main.quit_app()

            # Relist the options in the Book Transactions
            else:
                continue
        except Exception as e:
            print('ERROR: ', e)
