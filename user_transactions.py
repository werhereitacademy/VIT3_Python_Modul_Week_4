import main


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


def user_info(name):
    pass


def list_users(userlist):
    pass


def add_user(userlist: list):
    full_name = input('Enter user full name: ')
    phone = input('Enter user phone number: ')
    address = input('Enter user adress: ')

    if main.check_file(user_file_path):
        # print(user_list)
        id = userlist[-1]['id']
        print(id)
        a_user = {'id': id + 1,
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
    return a_user, userlist


def update_user(file_path, id_):
    userlist = main.read_from_json(file_path)

    for i in userlist:
        print(i['id'], type(i['id']))
        if i['id'] == id_:
            n_name = input(f'Enter new name for {i['full_name']}:')
            i['phone'] = input(f'Enter new phone for {i['full_name']}: ')
            i['address'] = input(f'Enter new address for {i['full_name']}: ')
            i['full_name'] = n_name
            main.write_to_json(file_path, userlist)
            result = i
        else:
            print('The user doesn\'t exist that you want to update!')
            result = 'No return list'
        return result


def search_user(file_path, name: str):
    userlist = main.read_from_json(file_path)
    n_userlist = []
    for user in userlist:
        if name.lower() in user['full_name'].lower():
            n_userlist += [user]
    return n_userlist


def delete_user(id):
    pass


def lend_book():
    pass


def return_book():
    pass


def track_book():
    pass


if __name__ == '__main__':

    activity = -1
    book_file_path = 'kitap.json'
    user_file_path = 'users.json'

    # while True:
    # try:
    #    splash_screen()
    # except Exception as e:
    #    print('ERROR: ', e)
    while activity != 9:
        activity = splash_screen()

        # List all books information
        if activity == '1':
            user_list = main.read_from_json(user_file_path)  # Fetch list from the file
            list_users(user_list)  # Send the list for listing process
            input('Press an any key to continue...')

        # Add a new user to the library system
        elif activity == '2':
            user_list = []
            if main.check_file(user_file_path):
                user_list = main.read_from_json(user_file_path)  # Fetch list from the file
            user_i, user_list = add_user(user_list)  # Send the list for adding process
            main.write_to_json(user_file_path, user_list)  # Write the updated list to the file
            input('Press an any key to continue...')

        # Update a user information in the library system
        elif activity == '3':  ####  cozulmedi!!!!!
            the_id = ''
            if main.check_file(user_file_path):
                the_user = input('Type the name of the person you want to update: ')
                the_user_list = search_user(user_file_path, the_user)

                if len(the_user_list) > 1:  #Adding extra info, if there are more results
                    print('There are multiple results based on your search criteria! Here you are:\n')
                    for the_user in the_user_list:
                        print(f'ID: {the_user['id']}\n'
                              f'{the_user['full_name']}\n'
                              f'{the_user['phone']}\n'
                              f'{the_user['address']}\n\n')
                    the_id = int(input("Enter the ID number of the user you want to update:"))
                else:
                    print(f'ID: {the_user_list[0]['id']}\n'
                          f'{the_user_list[0]['full_name']}\n'
                          f'{the_user_list[0]['phone']}\n'
                          f'{the_user_list[0]['address']}\n\n')
                    the_id = the_user_list[0]['id']
                    updated_user = update_user(user_file_path, the_id)

                print(f'The user is updated as: ', updated_user)
            else:
                print('Users data file doesn\'t exist!!!')
            input('Press an any key to continue...')

        # Search a user in the library system
        elif activity == '4':
            if main.check_file(user_file_path):
                the_user = input('Type the name of the person you want to get information about him/her: ')
                the_user_list = search_user(user_file_path, the_user)

                print('Found user(s) information:')
                for the_user in the_user_list:
                    print(f'{the_user['full_name']}\n'
                          f'{the_user['phone']}\n'
                          f'{the_user['address']}\n\n')
            else:
                print('The users\' data file doesn\'t exist!!!')
            input('Press an any key to continue...')
