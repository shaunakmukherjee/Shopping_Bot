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
    rating = soup.find_all(True, {"class" : "hide-content"})
    print " All books displayed by the search results are : --> \n"
    for i in range (len(bookname)) :
        print i+1, bookname[i].text.encode("utf-8","ignore"), author[i].text.encode("utf-8","ignore"), rating[i].text.encode("utf-8","ignore")    
    option = input("Enter a choice! \n")
    
    # taking the raw input and then calling the addtobag function with book and option
    
    #book = bookname[option]
    AddtoBag(option)
    
    #f = open('tempfile', 'w')
    #f.write(soup)

def AddtoBag (option) :
    
    # the book name has to be concatenated by '-''s between titles (e.g.thousand-suns-khaled-hossaini, etc.
    url = 'http://www.barnesandnoble.com/w/thousand-splendid-suns-khaled-hosseini/1100311165?ean=9781594483851'
    print "new url=> ", url
    c = requests.get(url).text
    soup = bs(c, "lxml")
    # print soup

    # now extracting elements

    detailed_review = soup.find(True, {"class" : "flexColumn"})
    current_price = soup.find(True, {"class" : "price current-price"})
    old_price = soup.find(True, {"class" : "old-price"})
    discount = soup.find(True, {"class" : "discount-amount"})
    print "Review of the book -->\n", detailed_review.text.encode("utf-8")
    print "Old Price --> ", old_price.text.encode("utf-8") 
    print "\nCURRENT PRICE --> ", current_price.text.encode("utf-8")
    print "\n",discount.text.encode("utf-8"), "!!"
    

    addtobag = soup.find(True, {"class" : "btn-addtocart btn-pdp-addtocart"})
    print "Do you want to add to cart? -> ", addtobag

    # if he wants to add to cart, the program goes to the shipping / form fillup page, otherwise back to menu
    #buyornot = input("Do you want to proceed? \nPress Y to proceed, N to go back to menu");

    #if buyornot == 'Y' : 
    Shipping ()


    #<input name="/atg/commerce/order/purchase/CartModifierFormHandler.catalogRefIds" value="9781594483851" type="hidden"><input name="_D:/atg/commerce/order/purchase/CartModifierFormHandler.catalogRefIds" value=" " type="hidden"><input value="Add to Bag" class="btn-addtocart btn-pdp-addtocart" type="submit">


# method to fill out form and ship

def Shipping () :
    
    url = 'https://www.barnesandnoble.com/checkout/shipping.jsp?_requestid=*'

    global fname, lname, address, suite, city, state, zip, phone, company
    print "\nshipping URL => ", url
    #c = requests.get(url).text
    #soup = bs(c, "lxml")
    #print soup

    # new soup of fill out form as guest

    #let's extract elements now !
    
    lines = [] # declaring an empty list to store lines

    userdata = open('userdata.txt')
    lines = userdata.readlines()

    fname = lines[0]
    lname = lines [1]
    address = lines [2]
    suite = lines [3]
    city = lines [4]
    state = lines [5]
    zip = lines [6]
    phone = lines [7]
    company = lines [8]

    print "\n===============USER DETAILS CONFIRMATION=================\n";
    print "\nFirst Name - ",fname,"\nLast name - ", lname,"\nAddress - ",address, "\nSuite - ",suite,"\nCity - ", city, "\nState - ",state
    print "\nZIP - ", zip, "\nPhone - ", phone, "\nCompany - ",company
    print "=============================================================";
    print "\n\nItem will be shipped to this address!"




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
        

