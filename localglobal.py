'''x = 10
def my_function():
    global x
    x = 4
    y = 5
    print(y)
my_function()
print(x)'''

f = open("myfile.txt","r")
i=0
while True:
    i = i +1
    file = f.readline()
    if not file:
       break
    m1 = int(file.split(",")[0])
    m2 = int(file.split(",")[1])
    m3 = int(file.split(",")[2])
    print(f"Marks of student {i} in maths is :{m1*2}")
    print(f"Marks of student {i} in english is :{m2*2}")
    print(f"Marks of student {i} in sst is :{m3*2}")
    print(file)
