#--------------------------------------------------------------------------------------------#
#------------------------------------- CALCULATOR -------------------------------------------#
import math

def add( x, y):
    return x + y

def sub( x, y):
    return x - y

def multi( x, y):
    return x * y       

def div( x, y):
    if y == 0:
        print("Error! Division by zero.")
    return x / y

def percentage(x,y):
    return (x + y)/100

def mod(x,y):
    return x % y

def SI( Per ,Rate, Time):
    return (Per*Rate*Time)/100

def square(x):
    return x ** x

def root(x):
    return math.sqrt(x)


def calculator():
    print("\n------- SELECT AN OPERATION -------")
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Percentage")
    print("6. Modulous")
    print("7. Square")
    print("8. Square Root")
    print("9. Simple Interest")

    choice = input("\nEnter choice ( 1 / 2 / 3 / 4 / 5 / 6 / 7 / 8 / 9) : ")

    if choice in ['1', '2', '3', '4','5','6']:

        num1 = float(input("Enter first number : "))
        num2 = float(input("Enter second number : "))

        if(choice == '1'):
            print("Sum is : ",add(num1,num2))


        elif(choice == '2'):
            print("Difference is : ",sub(num1,num2))

        
        elif(choice == '3'):
            print("Multiplication is : ",multi(num1,num2))

        
        elif(choice == '4'):
            print("Division is : ",div(num1,num2))

        
        elif(choice == '5'):
            print("Percentage is : ",percentage(num1,num2))

        
        elif(choice == '6'):
            print("Modulous is : ",mod(num1,num2))

        else:
            print("Invaild Choice ....")

    if choice == '7':
        x=float(input("Enter the Number : "))
        print("Square of the number is : ",square(x))

    elif choice == '8':
        x=float(input("Enter the Number : "))
        print("Square Root of the Number is : ",root(x))      
        
    if choice == '9':
        Per = float(input("Enter Percentage : "))
        Rate = float(input("Enter Rate : "))
        Time = float(input("Enter Time : "))
        print("Simple Interest is : ",SI(Per,Rate,Time))


if __name__== "__main__":
    calculator()





              


