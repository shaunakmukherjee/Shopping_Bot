import requests
from bs4 import BeautifulSoup as bs


# Base function to create a query and send it to 
# webserver. Modify this later to include this as
# seperate python file.

def shopper(book_name) :
    bookname = book_name.lower()
    bookName = '+'.join(bookname.split())
    url = 'http://www.barnesandnoble.com/s/' + bookName + '?_requestid=*'
    print "url: ", url
    content = requests.get(url).text
    #print content
    soup = bs(content, "lxml")
    #print soup
    author = soup.find_all(True, {"class" : "contributors"})
    bookname = soup.find_all(True, {"class" : "product-info-title"})
    print " All books displayed by the search results are : --> \n"
    for i in range (len(author)) :
        print i+1, bookname[i].text.encode("utf-8","ignore"), author[i].text.encode("utf-8","ignore")
    #f = open('tempfile', 'w')
    #f.write(soup)

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


