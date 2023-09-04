# Public => have access to all classes (i.e.) Outside the class where it's declared
# Public don't have any special syntax. you can siply write the class members names over there.

# Protected => have special syntax are written as : _classMemberName , _variableName , _methodName
# Protected have access till the derived classes within hierarchy. all derived classes have access to it.

# Private => Private don't have access directly to the derived and other classes as well.
# Private have access till only the same class they're written in.
# Special syntax to write Private are : __variableName , __methodName

# Example

class Car:
    manufacturer = "BMW"
    __serialNumber = 12354
    _country = "Germany"


class Gadi(Car):
    def __int__(self):
        print("This is the car named as X1\nThis is made by{}\tThe country in which this car is made is{}".format(self.manufacturer, self.country))


xone = Gadi()