class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    def get_size(self):
        return self._size

    def set_size(self, size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

   
    size = property(get_size, set_size)

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
        
# The Shoe class defines a shoe object. The shoe object has two attributes: brand and size. The brand attribute is a string that represents the brand of the shoe. The size attribute is an integer that represents the size of the shoe.

#The __init__() method initializes the Shoe object. The __init__() method takes two arguments: brand and size. The brand argument is the brand of the shoe. The size argument is the size of the shoe.

#The get_size() method returns the value of the size attribute. The set_size() method sets the value of the size attribute. The set_size() method validates the value of the size argument, ensuring that it is an integer.

#The size property is a special type of attribute that can be used to get or set the value of an attribute. The size property is defined using the property() decorator. The property() decorator takes two arguments: the get_size() method and the set_size() method.

#The cobble() method simply prints a message that says "Your shoe is as good as new!".

#The property() decorator is a way to create a property that has the same behavior as the get_size() and set_size() methods. The property() decorator takes two arguments: the get_size() method and the set_size() method. The property() decorator creates a property that can be used to get or set the value of the size attribute.