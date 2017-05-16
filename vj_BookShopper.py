import requests
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
    

    print " NUMBER" ," " * 5,"BOOK NAME"," " * 20, "AUTHOR"
    print "","-" * 60
    for i in range(len(bookList)):
        print i+1 ," " * 5,bookList[i]["title"]," " * 20,bookList[i]["author"]

    
def AddtoBag (option, book) :
    
    # the book name has to be concatenated by '-''s between titles (e.g.thousand-suns-khaled-hossaini, etc.
    url = 'http://www.barnesandnoble.com/w/' + book + '/*ean=*'
    print "new url=> ", url


def welcomeMenu() :
    print " ============================================================"
    print " ************** 600.466 Automatic BookShopper ***************" 
    print " ============================================================"
    print "1. Select to enter the Book Name"
    print "2. Select to Enter the Author Name"
    print "3. Select to get the reviews of a book"
    print "4. Exit"
    print 67 * "-"

loop=True

while loop:
    welcomeMenu()
    option = input("Enter choice: ")
    if option == 1 :
        print "Enter the name of the book you wish to buy: "
        bookName = raw_input()
        print "entered book name is: ", bookName
        shopper(bookName)
