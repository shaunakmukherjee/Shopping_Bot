import requests
from bs4 import BeautifulSoup as bs


#handles Billing part of the Bot

def Billing () :
    print "Sup"    
    url = 'http://www.barnesandnoble.com/w/thousand-splendid-suns-khaled-hosseini/1100311165?ean=9781594483851'
    print "url: ", url
    content = requests.get(url).text
    soup = bs(content, "lxml")
    #soup is created
    print soup 
    #bookname = soup.find_all(True, {"class" : "product-info-title"})
    
    #for i in range (len(bookname)) :
     #   print i+1, bookname[i].text.encode("utf-8","ignore"), author[i].text.encode("utf-8","ignore"), rating[i].text.encode("utf-8","ignore")    
    #option = input("Enter a choice! \n")
    

