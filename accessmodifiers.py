class Employee:
    def __init__(self):
        self.__name = "Harry"
a = Employee()
#print(a.__name)  error
print(a._Employee__name)#private running code
print(a.__dir__()) #mangling
