a = input("Enter a number:")
print(f"multiplication table of {a} is :")
try:
  for i in range(1,11):
    print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("Invalid input")

def func1():
    try:
        l=[1,2,3,4]
        i=input("enter a number:")
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
x=func1()
print(x)


a = input("Enter a number between 5 and 9:")
if (int(a)<5 or int(a)>9):
    raise ValueError("Value should be between 5 and 9")
elif a!="quit":
    raise ValueError("enter other value than quit")