class A:
    def method1(self):
        print("This is from class A")

    pass


class B(A):
    def method1(self):
        print("This is from class B")
    pass


class C(A):
    def method1(self):
        print("This is from class C")
    pass


class D(B, C):
    pass


dd = D()
dd.method1()

# In this cse the method resolution depends on the order in which the base class is inherited from the super classes