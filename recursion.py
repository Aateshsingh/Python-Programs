def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return(n* factorial(n-1))
n=5
print("factorial:",factorial(n))


data = {"Harry" , 1 , "Marks"}
for value in data:
    print(value)
