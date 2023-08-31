# Python OOP
# Classes are logical collection of attributes and methods() / actions() performed by that class
# Objects are instances of those classes
# Object instantiation
# Class definition in python
# Object creation
# Class attributes and instance attributes
# Class attribute should contain the data which is common to all of your class instances
class Employee:

    name = "RAJAN"
    phone = 919091919192
    active = True

    def is_active(self):
        if self.active:
            print("Employee status is active")
        else:
            print("Employee status is not active")


class_obj = Employee()
class_obj.is_active()
print("Name is : "+class_obj.name+" \nPhone number is "+str(class_obj.phone))


class Employee:

    Org = "MARS & CO"
    NO_work = 10


Emp_1 = Employee()
Emp_2 = Employee()
print(Emp_2.Org, Emp_1.Org)
Emp_2.Name = "JOHN"  # Instance attributes ?
Emp_1.Name = "DREW"  # Instance attributes ?
Emp_2.NO_work = 10
print(Emp_2.Name, Emp_1.Name, Emp_2.NO_work)
Emp_2.NO_work = 5
print(Emp_2.NO_work)
print(Emp_1.NO_work)    # Checks if the No_work is instance variable in that instance. If not checks within class


class Employee:
    def details(self):
        pass


emp = Employee()
Employee.details()