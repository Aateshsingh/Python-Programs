class person:
    def __init__(self,n,o):
        print("Hey I am a person")
        self.name = n
        self.occ = o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a = person("Harry","Developer")
b = person("Nikita","HR")
a.info()
b.info()

