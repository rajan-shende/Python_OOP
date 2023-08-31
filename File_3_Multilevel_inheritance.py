# Multiple inheritance
# Consider an scenario your grandpa was good at solving riddles and your father is good at playing football
# you as base class can have both properties inherited since your grandpa like can solve riddles as well as can play football very good
# The base classes we can say are subset of the superclass

# Example of multilevel inheritance


class Musical_instruments:
    No_tones = 7

class Guitar(Musical_instruments):
    type_wood = "Tone wood"


class Electric_guitar(Guitar):
    def __init__(self):
        print("The guitar is made up of {}\n The total number of tones is {}".format(self.type_wood, self.No_tones))

guitar = Electric_guitar()