class Employee:
    def __init__(self,name):
        self.name = name
    def __len__(self):
        i = 0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"The name of the employee is {self.name}"
e = Employee("Harry")
print(e.__str__)
print(e)