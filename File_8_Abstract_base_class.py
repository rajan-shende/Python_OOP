from abc import ABCMeta , abstractmethod
# Abstract class forces you to implement the methods contained within.
# It will throw error at runtime if those methods are not implemented.
# Also we're not suppose to create the objects for abstract class as it will result in error. Because class with abstract methods can not be initialised
# Abstract methods don't have any implementations within those are just defined.
# The implementation for abstract methods is decided at runtime.
# To define a class as abstract in python we can use abc module & ABCMeta class in python
# to mark a method as a abstract method we use decorator @abstractmethod
# to declare a class as abstract class we can use (metaclass = ABCMeta) declaration

class Shape(metaclass = ABCMeta):
    @abstractmethod
    def areaCal(self):
     return 0

class Square(Shape):
    side = 10
    def areaCal(self):
        print("Area of square is : ", self.side * self.side)

class Rectangle:
    length = 10
    width = 20
    def areaCal(self):
        print("Area of rectangle is : ", self.length * self.width)

sq = Square()
sq.areaCal()

rect = Rectangle()
rect.areaCal()


