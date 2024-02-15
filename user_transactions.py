import main


def splash_screen():
    print(
        '-' * 59, '\n' +
        '-', ' ' * 18, 'BOOK TRANSACTIONS', ' ' * 18, '-\n'
        '-', ' ' * 55, '-\n'
        '-', ' ' * 4, '-> LIST USERS    1', ' ' * 6, '-> BOOK LEND      5', ' ' * 4, '-\n'
        '-', ' ' * 4, '-> ADD USER      2', ' ' * 6, '-> BOOK RETURN    6', ' ' * 4, '-\n'
        '-', ' ' * 4, '-> SEARCH USER   3', ' ' * 6, '-> BOOK TRACK     7', ' ' * 4, '-\n'
        '-', ' ' * 4, '-> REMOVE USER   4', ' ' * 6, '-> EXIT           0', ' ' * 4, '-\n'
        '-', ' ' * 55, '-\n' +
        '-' * 59)
    return input()


if __name__ == '__main__':

    activity = -1
    book_file_path = 'kitap.json'

    while True:
        try:
            splash_screen()
        except Exception as e:
            print('ERROR: ', e)
