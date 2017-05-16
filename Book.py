"""
Book.py: This provides a book class to stire the details of the books.
        These objects are used at several instances of the shopping
        program.

Author: Vijaya Ram Illa
        Shaunak Mukherjee
"""

class Book :
    def __init__(self, author, title, url):
        self.bookInfo = {}
        self.bookInfo["author"] = author
        self.bookInfo["title"] = title
        self.bookInfo["url"] = url
        self.bookInfo["quantity"] = 0
        pass

    def getTitle(self) :
        return self.bookInfo["title"]

    def getAuthor(self) :
        return self.bookInfo["author"]

    def getURL(self) :
        return self.bookInfo["url"]

    def incrementQuantity() :
        self.bookInfo["quantity"] += 1



