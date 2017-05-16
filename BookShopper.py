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
    # ask user to select a book
    """
    bookNo = input("Slect the book number to checkout or press enter exit to main menu: ") 
    if option == "" :
        return
    else :
        addToBag(bookList, bookNo)
    """
def displayResults(bookList) : 

    print " ============================================================"
    print " ***************** LIST OF RETRIVED BOOKS   *****************"
    print " ============================================================"
    

    print " NUMBER" ," " * 5,"BOOK NAME"," " * 20, "AUTHOR"
    print "","-" * 60
    for i in range(len(bookList)):
        #print i+1 ," " * 5,bookList[i]["title"]," " * 20,bookList[i]["author"]
        print i+1 ," " * 5,bookList[i].getTitle()," " * 20,bookList[i].getAuthor()

"""    
def addToBag (bookList, bookNo) :
    print "Selected Book: ", bookList[bookNo - 1]["title"], " by ", bookList[bookNo - 1]["author"]
    newURL = 'http://www.barnesandnoble.com/s/' + bookList[bookNo - 1]["url"]
    content = requests.get(newURL).text
    soup = bs(content, "lxml")
    print soup.prettify()
    detailed_review = soup.find(True, {"class" : "flexColumn"})
    current_price = soup.find(True, {"class" : "price current-price"})
    discount = soup.find(True, {"class" : "discount-amount"})
    print "Review of the book -->\n", detailed_review.text.encode("utf-8")
    print "\nCURRENT PRICE --> ", current_price.text.encode("utf-8")

    proceed = raw_input("Add the book to the shopping bag?(y/n):  ")
    if raw_input == y :
        #proceed to pay
        return 
    else :
        #call display results function to display results again
        return
"""    

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
