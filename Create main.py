from book_file import *
from member_file import *
import json
from my_time import *
from datetime import datetime, timedelta
import os

while True:
    choice = input(
        "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀" +
        "\n≀                                                                                ≀" +
        "\n≀   Press 1 for Membership Operations                                            ≀" +
        "\n≀   Press 2 for Book Operations                                                  ≀" +
        "\n≀   Press 0 to Exit                                                              ≀" +
        "\n≀                                                                                ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~≀")
    if choice == "1":
        choice1 = input(
            "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ≀" +
            "\n≀                                                                           ≀" +
            "\n≀   Press 1 for Members             Press 5 to Borrow a Book                ≀" +
            "\n≀   Press 2 to Add a Member         Press 6 to Return a Book                ≀" +
            "\n≀   Press 3 to Search for a Member  Press 7 for Book Tracking               ≀" +
            "\n≀   Press 4 to Delete a Member      Press 0 to Exit                         ≀" +
            "\n≀                                                                           ≀" +
            "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ≀")
        if choice1 == "1":
            members()
        elif choice1 == "2":
            add_member()
        elif choice1 == "3":
            search_member()
        elif choice1 == "4":
            delete_member()
        elif choice1 == "5":
            borrow_book()
        elif choice1 == "6":
            return_book()
        elif choice1 == "7":
            book_tracking()
        elif choice1 == "0":
            continue

    elif choice == "2":
        choice2 = input(
            "≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~  ≀" +
            "\n≀                                                                          ≀" +
            "\n≀   Press 1 for Books                                                      ≀" +
            "\n≀   Press 2 to Add a Book                                                  ≀" +
            "\n≀   Press 3 to Search for a Book                                           ≀" +
            "\n≀   Press 0 to Exit                                                        ≀" +
            "\n≀                                                                          ≀" +
            "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~~ ~ ~ ~ ~ ≀")

        if choice2 == "1":
            view_books()
        elif choice2 == "2":
            add_book()
        elif choice2 == "3":
            search_book()
        elif choice == "0":
            continue
    elif choice == "0":
        break
