x=int(input("Enter a number to search:"))
match x:
    case 0:
        print("The case is zero")
    case 4:
        print("The case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")