class Person:
    Name = "Harry"
    Occupation = "Software developer"
    Networth = 1000
    def info(self):
        print(f"{self.Name} is a {self.Occupation}")

a = Person()
#a.Name = "Subham"
#a.Occupation = "Accontant"
#print(a.Name,a.Occupation)
a.info()
