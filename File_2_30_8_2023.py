# Instance methods and static methods
# Instance methdods usually deals with the instance of that particular class.
# Instance methods usually deals stuff like Like changing class attributes and other things
# Instance methods are by default passed self parameter refering to the current instance of the class
# to make methods static we use @staticmethod decorator.
# static methods are ignored at time of binding

class Employee:
    name = ""
    id = ""

    def upadte_details(self, name_1, id_1):
        self.name = name_1
        self.id = id_1
    @staticmethod
    def welcome_msg():
        print("Welcome to class employee")


emp = Employee()
print(emp.id, emp.name)
emp.upadte_details("RAJAN", 123)
print(emp.id, emp.name)
emp.welcome_msg()

# Init method to initialize class attributes at runtime
# it's written as with __ at starting and end
# there will be issue if a class have 2 different methods 1 to initialise &
# other method to display. If we call the
# print method before initialization it will raise error


class Employee:
    name = "RAJAN"
    id = 1232

    def assign_location(self, location):
        self.location = location

    def display_details(self):
        print("id is :"+str(self.id)+"\n"+"Name is : "+str(self.name))

# Example of init method


class Employee:
    org = "MARS & CO"

    def __int__(self, name, id):
        self.name = name
        self.id = id

emp = Employee("RAJAN", 123)