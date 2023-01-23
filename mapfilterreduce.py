def cube(x):
    return x*x*x
l = [1,2,4,6,4,3]
#l1 =[]
#for item in l:
#    l1.append(cube(item))
l1 = list(map(cube,l))
print(l1)

def filter_function(a):
    return a>4
l2 = list(filter(filter_function,l))
print(l2)

from functools import reduce
numbers = [1,2,3,4,5]
sum = reduce(lambda x,y: x+y,numbers)
print(sum)
