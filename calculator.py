num1 = input("CALCULATOR:\n\n\n\nEnter the first number you wish to input: ")
operator = input('''\nType the number corresponding to the operation you want to use:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent
6. Root

Enter here: ''')
num2 = input("\nEnter the second number you wish to input: ")

try:
    if num1.isdigit():
        num1 = int(num1)
    else:
        num1 = float(num1)
    if num2.isdigit():
        num2 = int(num2)
    else:
        num2 = float(num2)
except:
    print("ERROR: Numbers must be a digit.")
    exit()

try:
    if operator == "1":
        print(f"\n{num1} + {num2} = {num1 + num2}")
    elif operator == "2":
        print(f"\n{num1} - {num2} = {num1 - num2}")
    elif operator == "3":
        print(f"\n{num1} * {num2} = {num1 * num2}")
    elif operator == "4":
        print(f"\n{num1} / {num2} = {num1 / num2}")
    elif operator == "5":
        print(f"\n{num1} ^ {num2} = {num1 ** num2}")
    elif operator == "6":
        if num1 >= 0:
            print(f"\n{num1} // {num2} = {num1 ** (1 / num2)}")
        else:
            print(f"\n{num1} // {num2} = {abs(num1) ** (1 / num2)}i")
    else:
        print('ERROR: Operator has to be a number from 1 to 6.')
        exit()
except:
    if operator == "1" or "2" or "3" or "4" or "5" or "6":
        print(f"\n{num1} {operator} {num2} = Undefined")
        exit()