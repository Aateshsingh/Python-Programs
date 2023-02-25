class Employee:
    company = "Apple"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}")
    @classmethod
    def changecompany(cls,newCompany):
        cls.company = newCompany
e1 = Employee()
e1.name = "Harry"
e1.show()
e1.changecompany("Tesla")
e1.show()
print(Employee.company)