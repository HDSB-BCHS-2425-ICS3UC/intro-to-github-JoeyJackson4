operation = int(input("type 0 for +, type 1 for -: "))

if(operation == 0):
    number1 = int(input("enter your first number: "))
    print(number1)
    number2 = int(input("enter your second number: "))
    print(number2)
    confirm = int(input("please confirm your answer type 1, if not type 0: "))
    if(confirm == 1):
        print("The answer is:",number1+number2)
    if(confirm == 0):
        print("please restart")
    
if(operation == 1):
    number1 = int(input("enter your first number: "))
    print(number1)
    number2 = int(input("enter your second number: "))
    print(number2)
    confirm = int(input("please confirm your answer type 1, if not type 0: "))
    if(confirm == 1):
        print("The answer is:",number1-number2)
    if(confirm == 0):
        print("please restart")
    