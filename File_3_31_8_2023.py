# Inheritance
# Single Inheritance

class Apple:
    manufacturer = "Apple .INC"
    website = "www.apple.co"

    def display(self):
        print("Iphone is our product :\n{} To contact us visit :{}".format(self.manufacturer, self.website))


class Macbook(Apple):  # to inherit from base class we've to use () after child class name and pass base class name
    def __init__(self):
        self.Year_manufacturer = "2019"

    def print_details(self):  # In this function the python will check for manufacturer if this is not found in current class; it will go to base class and checks for it.
        print("This mackbook was manufacturered by {} in year {}".format(self.manufacturer, self.Year_manufacturer))


#apple = Apple()
#apple.display()

mac =Macbook()
mac.print_details()
mac.display()

