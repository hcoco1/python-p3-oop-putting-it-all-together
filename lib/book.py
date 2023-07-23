class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")

    page_count = property(get_page_count, set_page_count)

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

            
#The Book class defines a book object. The book object has two attributes: title and page_count. The title attribute is a string that represents the title of the book. The page_count attribute is an integer that represents the number of pages in the book.

# The __init__() method initializes the Book object. The __init__() method takes two arguments: title and page_count. The title argument is the title of the book. The page_count argument is the number of pages in the book.

# The get_page_count() method returns the value of the page_count attribute. The set_page_count() method sets the value of the page_count attribute. The set_page_count() method validates the value of the page_count argument, ensuring that it is an integer.

# The page_count attribute is a property. A property is a special type of attribute that can be used to get or set the value of an attribute. The page_count property is defined using the property() decorator. The property() decorator takes two arguments: the get_page_count() method and the set_page_count() method.

# The turn_page() method simply prints a message that says "Flipping the page...wow, you read fast!".      
        