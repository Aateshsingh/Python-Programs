x =" My name is {} and I am from {}"
a="Aatesh"
b="India"
c = x.format(a,b)
print(c)
print(f"My name is {a} and I am from {b}")

def square(n):
    '''Takes in a number n, return the square root of n'''
    print(n**2)
square(5)
print(square.__doc__)

#import this