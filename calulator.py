operation = int(input("type 0 for +, type 1 for -, type 2 for *, type 3 for /, type 4 for **: "))

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
    #this is for additon and getting the users input.

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
        #this is for subtraction and getting the user input.

if(operation == 2):
    number1 = int(input("enter your first number: "))
    print(number1)
    number2 = int(input("enter your second number: "))
    print(number2)
    confirm = int(input("please confirm your answer type 1, if not type 0: "))
    if(confirm == 1):
        print("The answer is:",number1*number2)
    if(confirm == 0):
        print("please restart")
        #this is for multiplication and getting the user input.

if(operation == 3):
    number1 = int(input("enter your first number: "))
    print(number1)
    number2 = int(input("enter your second number: "))
    print(number2)
    confirm = int(input("please confirm your answer type 1, if not type 0: "))
    if(confirm == 1):
        print("The answer is:",number1/number2)
    if(confirm == 0):
        print("please restart")
        #this is for division and getting the user input.

if(operation == 4):

    number1 = int(input("enter your first number: "))
    print(number1)
    number2 = int(input("enter your second number: "))
    print(number2)
    confirm = int(input("please confirm your answer type 1, if not type 0: "))
    if(confirm == 1):
        print("The answer is:",number1**number2)
    if(confirm == 0):
        print("please restart")
        #this is for power of and getting the user input.
