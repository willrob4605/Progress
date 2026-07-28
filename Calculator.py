"Make a calculator that loops but exits with the quit keyword"
First=False
result=None
# def Divide(num1,num2):
#     return num1/num2
# def Add(num1,num2):

def Main():
    num1=int(input("Enter your first number: "))
    num2=int(input("Enter your second number: "))
    print("Choose your operation to be done")
    print("1. +")
    print("2. -")
    print("3. /")
    print("4. *")
    print("5. quit")
    choice=int(input())
    while 1<=choice<=4:
        if choice==1:
            result=num1+num2
        if choice==2:
            result=num1-num2
        if choice==3:
            result=num1/num2
        if choice==4:
            result=num1*num2
        print(f"The Result is {result}")
        Main()
    if choice==5:
        print("Quitting...")
Main()

    