import requests
import sys
from bs4 import BeautifulSoup as bs
from bookSearchQuery import bookSearch
from Book import *

# Base function to create a query and send it to 
# webserver. Modify this later to include this as
# seperate python file.

def shopper(book_name) :
    bookname = book_name.lower()
    bookName = '+'.join(bookname.split())
    url = 'http://www.barnesandnoble.com/s/' + bookName + '?_requestid=*'
    bookList = bookSearch(url)

    #call the print function
    displayResults(bookList)
    """
    for i in range(len(bookList)):
        info = bookList[i]
        print "book no: ", i
        print info
    """
def displayResults(bookList) : 

    print " ===================================+========================================="
    print " ************************* LIST OF RETRIVED BOOKS   **************************"
    print " ============================================================================="
    

    print " NUMBER" ," " * 5,"BOOK NAME"," " * 35, "AUTHOR"
    print "","-" * 60
    for i in range(len(bookList)):
        print i+1 ," " * 7,bookList[i]["title"]," " * 20,bookList[i]["author"]

    choice = input("\nWhich book do you want? Please enter its number, or press 0 to exit to the main menu!\n")
    if choice == 0 :
        welcomeMenu()
    else :
        review(bookList, choice)


# function given to search according to author name

def author_search(author_name) :
    authorname = author_name.lower()
    authorName = '+'.join(authorname.split())
    url =  'http://www.barnesandnoble.com/s/' + authorName + '?_requestid=*'
    authorList = bookSearch(url)

    # like in the shopper, calling the print function
    displayResults(authorList)


# function to display review and other details of the book

def review (bookList, bookNo) :
    print "\n\nSelected Book : ", bookList[bookNo - 1]["title"], " by ", bookList[bookNo - 1]["author"]
    newURL = 'http://www.barnesandnoble.com/s/' + bookList[bookNo - 1]["url"]
    content = requests.get(newURL).text
    soup = bs(content, "lxml")
    #print soup.prettify()
    detailed_review = soup.find(True, {"class" : "flexColumn"})
    current_price = soup.find(True, {"class" : "price current-price"})
    discount = soup.find(True, {"class" : "discount-amount"})
    print "\n~~~~~~~~~~~~~~~~~~~~BOOK DETAILS~~~~~~~~~~~~~~~~~~~\n\n"
    print "\nReview of the book -->\n", detailed_review
    print "\n\nCURRENT PRICE --> ", current_price
    print "\n\nYou're getting a discount of ", discount
    
    ## ADD TO BAG FUNCTIONALITIES TO BE ADDED HERE
    
    choice_shipping = input("\n\nContinue to billing?\n\n 1 for YES, 0 for NO!\n\n")
    if choice_shipping == 0 :
        mainMenu()
    else :
        shipping(bookList, bookNo)
        
def AddtoBag (option, book) :
    
    # the book name has to be concatenated by '-''s between titles (e.g.thousand-suns-khaled-hossaini, etc.
    url = 'http://www.barnesandnoble.com/w/' + book + '/*ean=*'
    print "new url=> ", url


# method to start and end shipping process
def shipping(bookList, bookNo) :

    lines = [] # to display the lines
    with open("userdata.txt") as f :
        content = f.readlines()
    content = [x.strip() for x in content]
    fname = content[0]
    lname = content[1]
    address = content[2]
    suite = content[3]
    city = content[4]
    state = content[5]
    zip = content[6]
    phone = content[7]
    company = content[8]

    print "\n\n(Now reading data from file given)\n\n"
    print "\n\n=========================BILLING DETAILS==========================\n"
    print "First Name = ",fname,"\nLast Name = ", lname,"\nAddress = ",address,"\nCity = ", city, "\nState = ", state, "\nZIP = ",zip,"\nPhone Number = ",phone, "\nCompany Name = ",company
    print "ORDER DETAILS = \nBook Name : ", bookList[bookNo - 1]["title"],"\nAuthor = ", bookList[bookNo - 1]["author"]
    print "\n\n==================================================================\n"
    choice_final = input("\n\nDo you want to checkout? Press 1 for checking out and 0 if you want to go back and change any details!\n\n")
    if choice_final == 1 :
        print "\n\n=======================SUCCESS!!=====================\n\n Your Order has been successfully placed ! \nThank you so much for using our Shopping Bot !\n\n"
        print "\n\n(C) Shaunak Mukherjee and Vijayaram Illa, 2017.\n\n"
    sys.exit()

def welcomeMenu() :
    print " ======================================================================\n"
    print " ************ Welcome to the 600.466 Automatic BookShopper ************\n" 
    print " ======================================================================\n"
    print "1. Search books by the Book Name"
    print "2. Search books by the Author Name"
    print "3. Get the details (price / review) of a book"
    print "4. Exit"

loop=True

while loop:
    welcomeMenu()
    option = input("Enter choice: ")
    if option == 1 :
        print "Enter the name of the book you wish to buy: "
        bookName = raw_input()
        print "\n\nYou're currently searching for books named : ", bookName
        shopper(bookName)
    if option == 2 :
        print "Enter the name of the author whose book you wish to buy: "
        authorName = raw_input()
        print "\n\nYou're currently searching for books authored by : ", authorName
        author_search(authorName)
    if option == 4 :
        sys.exit()
