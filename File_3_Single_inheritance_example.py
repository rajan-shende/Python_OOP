class SwissBank:
    website = "www.swissbank.co"
    establishment = "1980"
    headquarters = "Switzerland"


class Branch1(SwissBank):
    def __init__(self):
        print("This is branch of Swissbank\nfor more details visit :\t{}".format(self.website))

branch1 = Branch1()
