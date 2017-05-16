import requests
import sys
from bs4 import BeautifulSoup as bs
from bookSearchQuery import bookSearch

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

    print " ============================================================"
    print " ***************** LIST OF RETRIVED BOOKS   *****************"
    print " ============================================================"
    

    print " NUMBER" ," " * 5,"BOOK NAME"," " * 30, "AUTHOR"
    print "","-" * 60
    for i in range(len(bookList)):
        print i+1 ," " * 7,bookList[i]["title"]," " * 20,bookList[i]["author"]

def author_search(author_name) :
    authorname = author_name.lower()
    authorName = '+'.join(authorname.split())
    url =  'http://www.barnesandnoble.com/s/' + authorName + '?_requestid=*'
    authorList = bookSearch(url)

    # like in the shopper, calling the print function
    displayResults(authorList)

    
def AddtoBag (option, book) :
    
    # the book name has to be concatenated by '-''s between titles (e.g.thousand-suns-khaled-hossaini, etc.
    url = 'http://www.barnesandnoble.com/w/' + book + '/*ean=*'
    print "new url=> ", url


def welcomeMenu() :
    print " ======================================================================\n"
    print " ************ Welcome to the 600.466 Automatic BookShopper ************\n" 
    print " ======================================================================\n"
    print "1. Search books by the Book Name"
    print "2. Search books by the Author Name"
    print "3. Get the reviews of a book"
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
