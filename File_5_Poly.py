class Employee:
    def noWorkingHours(self):
        self.noHours = 8

    def displayHours(self):
        print("No of working hours is {}".format(self.noHours))


class Trainee(Employee):
    def noWorkingHours(self):
        self.noHours = 45
    def displayHours(self):
        print("No of working hours is {}".format(self.noHours))
    def resetHours(self):
        super().noWorkingHours()




# emp = Employee()
# emp.noWorkingHours()
# emp.displayHours()

trainee = Trainee()
trainee.noWorkingHours()
trainee.displayHours()
trainee.resetHours()
trainee.displayHours()