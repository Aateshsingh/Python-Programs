x=int(input("Enter a number of terms:"))
a=0
b=1
print(a,b,end=" ")
for i in range(0,x):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

num = int(input("enter a number:"))
sum = 0
num2=str(num)
temp = num
powe=len(num2)
while num > 0:
    digit = num % 10
    sum += digit**powe
    num //= 10
if temp == sum:
    print(temp, "is amstrong")
else:
    print(temp, "is not amstrong")