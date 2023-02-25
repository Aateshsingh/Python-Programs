class Employee:
    companyName = "Apple" #class variable
    Noofemployee = 0
    def __init__(self,name):
        self.name = name
        self.raise_amount = 0.02
        Employee.Noofemployee +=1
    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.Noofemployee} sized {self.companyName} is {self.raise_amount}")
emp1 = Employee("Harry")
emp1.raise_amount = 0.3 #istance variable
emp1.companyName = "Apple India"
emp1.showDetails()
Employee.companyName = "Google"
emp2 = Employee("Rohan")
emp2.showDetails()
#Employee.showDetails(emp1)