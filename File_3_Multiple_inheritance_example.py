# Multiple inheritance in python
# If you are child and your dad was good at football & yuor mom was good at making omletes
# You as a child can be good at both of the above things ; Meaning you've inherited the parent properties
# Likewise in Python the base class can inherit the multiple properties from the multiple base classes.
# We in technical terms call it as multiple inheritance. Languages like JAVA do not support Multiple inheritance
# If we have same attribute in both of the classes from which we've inherited the base. Then The value of that attribute is used from the clss which is 1st in order given for multiple inheritance

# Example

class Apple:
    website = "www.apple.co"


class Os:
    Operating_system = "Apple 3.9"


class Macbok(Apple, Os):
    def __init__(self):
        print("This is mac book. Built in OS is : {} Product of Apple. Checkout more products on {}".format(self.Operating_system, self.website))

mac = Macbok()

# Example
class Apple:
    website = "www.apple.co"


class Os:
    website = "www.python.org"
    Operating_system = "Apple 3.9"


class Macbok(Os, Apple):
    def __init__(self):
        print("This is mac book. Built in OS is : {} Product of Apple. Checkout more products on {}".format(self.Operating_system, self.website))

mac = Macbok()








