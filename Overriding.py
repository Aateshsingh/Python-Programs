class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
rec = Shape(3,5)
print(rec.area())
