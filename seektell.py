'''with open("myfile.txt","r") as f:
    print(type(f))
    f.seek(10)
    print(f.tell())
    data = f.read(5)
    print(data)'''

double = lambda x: x*2
cube =  lambda x: x*x*x
avg = lambda x,y : (x+y)/2
print(avg(5,3))
print(cube(3))
print(double(5))