# Redefining your own operators.
# Here i'm overloading the Multiplication operator

class SquareNumber:
    def __init__(self, no):
        self.number = no

    def __mul__(no1, no2):
        return no1.number * no2.number


no1 = SquareNumber(10)
no2 = SquareNumber(10)

no3 = SquareNumber(20)
no4 = SquareNumber(20)

print(no1 * no2)
print(no3 * no4)