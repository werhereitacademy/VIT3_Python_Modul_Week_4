
#*********************Main**************************
import book_transactions as bt, time_operations as to, member_transactions as mt , json
from colorama import Fore, init
init(autoreset=True) 

while True: 
    print(f"""    {to.star(15)} {(Fore.GREEN + "Welcome to Library Management System")}{Fore.WHITE} {to.star(16)}                                                                    
    * Press 1 for membership transactions.                              *
    * Press 2 for book transactions.                                    *
    * Press 0 to exit.                                                  *
    {to.star(69)}""")

    process = input("Please enter process number=")

    if process == "1":
        while(True):
            print(f"""    {to.star(15)} {(Fore.GREEN + "Welcome to Members Management System")}{Fore.WHITE} {to.star(16)}
    * Press 1 for members.             ** Press 5 to lend a book.       *
    * Press 2 to add members.          ** Press 6 to return the book.   *
    * Press 3 to search for a member.  ** Press 7 to follow the book.   *
    * press 4 to delete the member.    ** Press 0 to exit.              *
    {to.star(69)}""")
            process = input("Please enter process number=")
            if process == "1":
                print(Fore.GREEN + "General Member List")
                mt.general_member_list()
            elif process == "2":
                name_member = input("Enter the member name :")
                tel_member = input("Enter the member tel :")
                address_member = input("Enter the member address :")
                mt.add_member(name_member,tel_member,address_member)
            elif process == "3":
                member_look = (input("Please enter member ID or member name or member phone or member address:")).lower()
                mt.search_member(member_look)
            elif process == "4":
                print(Fore.GREEN + "General Member List")
                mt.general_member_list()
                delete_id = input("Please enter delete member ID:")
                mt.delete_member(delete_id)
            elif process == "5":
                member_look = input("Please enter member ID or member name or member phone or member address:").lower()
                barcode_number = int(input("Please enter barcode number:"))
                mt.lend_book(member_look,barcode_number)
            elif process == "6":
                print(Fore.GREEN + "Lend Follow List")
                mt.lend_follow()
                mt.return_book()    
            elif process == "7":
                mt.lend_follow()   
            elif process == "0":
                break
            else:
                print(Fore.RED + "Please enter a number between 0 and 7") 
             
    elif process == "2":
        while(True):
            print(f"""    {to.star(17)} {(Fore.GREEN + "Welcome to Book Management System")}{Fore.WHITE} {to.star(17)}
    * Press 1 for the book list.                                        *
    * Press 2 to add a book.                                            *
    * Press 3 to search for a book.                                     *
    * Press 4 to delete for a book.                                     *
    * Press 0 to exit                                                   *
    {to.star(69)}""")

            process = input("Please enter process number=")
            if process == "1":
                bt.list_book(bt.book_list)
            elif process == "2":
                book_barcode = int(input("Enter book barcode :"))
                language = input("Enter the book language :")
                price = input("Enter the book price :")
                book_name = input("Enter the book name :")
                book_publishinghouse = input("Enter the book publishing house :")
                book_author = input("Enter the book author :")
                bt.add_book(book_barcode,language,price,book_name,book_publishinghouse,book_author)

            elif process == "3":
                bt.search_book()
            elif process == "4":
                barcode_number = int(input("Please enter barcode number:"))
                bt.delete_book(barcode_number)
                print(Fore.GREEN + "The book has been deleted successfully.")
                
            elif process == "0":
                break    
            else:
                print(Fore.RED + "Please enter a number between 0 and 4") 

    elif process == "0":
        break        
    else:
        print(Fore.RED + "Please enter a number between 0 and 2") 


#********************************book_transactions*********************          
import json, time_operations
from colorama import Fore, init
init(autoreset=True) 
book_list = [""]

def read():
   """ Read write function """
   with open('book.json', 'w') as json_book:
        json.dump(book_list,json_book, indent=6, sort_keys = True)
        print(Fore.GREEN + "All information was recorded.") 
try: 
    with open('book.json', 'r') as json_book:
        book_list = json.load(json_book)     
except FileNotFoundError:
    print(Fore.RED + "No data found.") 


def list_book(book_list):
    """This function is used to list books and lended books. """
    try:
        for book in book_list:
            print(f'{book["Barkod"]}--{book["Kitap_Adi"]}--{book["Yayinevi"]}--{book["Yazar"]}==ID==>{book["Id"]}')
    except KeyError:
        for book in book_list:
            print(f'{book["Barkod"]}--{book["Kitap_Adi"]}--{book["Yayinevi"]}--{book["Yazar"]}')                  
      

def add_book(book_barcode,language:'None',price:'None',book_name,book_publishinghouse,book_author):
    """ This function is used to add books and return books. """
    new_book = {
        "Barkod" : book_barcode,
        "Dil" :language,
        "Fiyat" :price,
        "Kitap_Adi" : book_name,
        "Yayinevi" : book_publishinghouse,
        "Yazar" : book_author,
    }
    book_list.append(new_book) 
    read()  


def search_book():
    """ Book search function """
    while(True):  
        print(f"""    {time_operations.star(25)} {(Fore.GREEN + "Welcome Book Search")}{Fore.WHITE} {time_operations.star(24)}                                                                    
    * Press 1 to search by barcode.                                      *
    * Press 2 to search by book title, author name or publishing house.  *
    * Press 0 to exit.                                                   *
    {time_operations.star(70)}""") 
        try:               
            process = int(input("Please enter process number:"))
            if process == 1:
                barcode_number = int(input("Please enter barcode number:"))
                count = 1
                for book in book_list:
                    if book["Barkod"] == barcode_number:    
                        print(f'{count}.){book["Barkod"]}--{book["Kitap_Adi"]}--{book["Yayinevi"]}--{book["Yazar"]}') 
                        count += 1       
                if count < 2:
                    print(Fore.RED + "Book Not Found")
        
            elif process == 2:
                book_look= (input("Please enter book title, author name or publishing house:")).lower()
                count = 1
                for book in book_list:
                    if book["Kitap_Adi"].lower() == book_look or book["Yayinevi"].lower() == book_look or book["Yazar"].lower() == book_look:
                        print(f'{count}).{book["Barkod"]}--{book["Kitap_Adi"]}--{book["Yayinevi"]}--{book["Yazar"]}')
                        count += 1               
                if count < 2:
                    print(Fore.RED + "Book Not Found")

            elif process == 0 :
                break 

            else:
                print(Fore.RED + "Please enter a number between 0 and 2") 
        except ValueError:
            print(Fore.RED + "Please Enter Number")
            
                         
def delete_book(barcode_number):
    """ This function is used to delete books and for lended books. """
    for book in book_list:
        if book["Barkod"] == barcode_number:    
            print(f'{book["Barkod"]}--{book["Kitap_Adi"]}--{book["Yayinevi"]}--{book["Yazar"]}')
            book_list.remove(book)
            read()
            break
    else:
        print(Fore.RED + "Book Not Found")        


#********************************member_transactions*************************
import json, time_operations as to, book_transactions as bt
from colorama import Fore, init
init(autoreset=True) 
list_member = ['']
list_follow = []


def read_member():
   """ Read write function for member """
   with open('member.json', 'w') as json_member:
        json.dump(list_member,json_member, indent=4)
        print(Fore.GREEN + "All information was recorded.") 
try: 
    with open('member.json', 'r') as json_member:
        list_member = json.load(json_member)
except FileNotFoundError:
    print(Fore.RED + "Membership Record Not Found.") 


def add_member(name_member,tel_member,address_member):
    """ Add member function """
    new_member = {
        "Id" :to.member_id(),
        "Member name":name_member,
        "Tel":tel_member,
        "Address" :address_member,
    }
    list_member.append(new_member)
    print(list_member) 
    read_member() 
        

def follow_read():
    """ Read write function for follow """
    with open('follow.json', 'w') as json_follow:
        json.dump(list_follow,json_follow, indent=4)
        print(Fore.GREEN + "All information was recorded.")        
try: 
    with open('follow.json', 'r') as json_follow:
        list_follow = json.load(json_follow)
except FileNotFoundError:
    print(Fore.RED + "Membership record not found")  


def search_member(member_look):
    """ Member search function """
    count = 1
    for member in list_member:
        if member["Id"].lower()== member_look or member["Member name"].lower() == member_look or member["Tel"].lower() == member_look or member["Address"].lower() == member_look:
            print(f'{count}.){member["Id"]}--{member["Member name"]}--{member["Tel"]}--{member["Address"]}')
            count += 1
    if count < 2 :                             
        print(Fore.RED + "Member Not Found")


def delete_member(delete_id):
    """ Member deletion function """
    for member in list_member:
        if delete_id == member["Id"]:
            list_member.remove(member)
            print(Fore.GREEN + "Member Successfully Deleted")
            read_member()
            break
    else:
        print(Fore.RED + "Membership record not found")


def general_member_list():
    """ General member list function """
    count = 1
    for member in list_member:
        print(f'{count}.) {member["Id"]}--{member["Member name"]}--{member["Tel"]}--{member["Address"]}')
        count += 1 

  
def lend_book(member_look,barcode_number):
    """ Book lend function """
    for member in list_member:
        if member["Id"].lower()== member_look or member["Member name"].lower() == member_look or member["Tel"].lower() == member_look or member["Address"].lower() == member_look:
            for book in bt.book_list:
                if book["Barkod"] == barcode_number:
                    date = {
                        "Lend date" : to.start_tijd(),
                        "Return date": to.end_tijd(),
                    }
                    new = member | book | date
                    list_follow.append(new)
                    bt.delete_book(barcode_number)         
                    follow_read()
                    break

    
def return_book():
    """ Return book function """
    barcode_number = int(input("Please enter barcode number:"))
    for book in list_follow:
        if book["Barkod"] == barcode_number: 
            bt.add_book(book["Barkod"],book["Dil"],book["Fiyat"],book["Kitap_Adi"],book["Yayinevi"],book["Yazar"])
            list_follow.remove(book)
            follow_read()

            
def  lend_follow():
    """Function that keeps track of loaned books """
    bt.list_book(list_follow)
   
  
          
                









    
    

     

