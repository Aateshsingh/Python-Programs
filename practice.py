print("***********  CALCULATOR  ************")
a=int(input("enter a number1:"))
b=int(input("enter a number2:"))
print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Quit")
ch=int(input("enter your choice:"))
if ch==1:
    print("The Addition of two numbers:",a+b)
elif ch==2:
    print("The Subtraction of two numbers is:",a-b)
elif ch==3:
    print("The Multiplication of two numbers is:",a*b)
elif ch==4:
    print("The Division of two number is:",a/b)
else:
    print("Invalid choice")

