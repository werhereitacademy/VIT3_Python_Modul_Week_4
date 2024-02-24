"""
- This program is used one time to update 'kitap.json' file for lending, return, and track processes.
- The new key - 'Kira_Durumu' - will be used for 'user_id' who borrows the book or 0 for the unlent book.
"""

import main


if main.check_file('kitap.json'):
    book_list = main.read_from_json('kitap.json')
    for book in book_list:
        book.update({'Kira_Durumu': 0})
    print(book_list)
    main.write_to_json('kitap.json', book_list)
else:
    print('There is no file to read!')
