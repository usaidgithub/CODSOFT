while True:
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print(f"The addition of the given number is {a+b}")
    elif(choice==2):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print(f"The substraction of the given number is {a-b}")
    elif(choice==3):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print(f"The multiplication of the given number is {a*b}")
    elif(choice==4):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        if(b==0):
            print("Cannot be divided by the zero")
        else:
            print(f"The division of the given number is {a/b}")
    elif(choice==5):
        a=float(input("Enter first number:"))
        b=float(input("Enter second number:"))
        print(f"The modulus of the given number is {a%b}")
    elif(choice==6):
        break
    else:
        print("Please enter a valid value")
