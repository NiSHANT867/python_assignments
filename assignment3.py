def calculator():
    
    print("1. Addition ")
    print("2. Subtraction ")
    print("3. Multiplication ")
    print("4. Division ")
    print("5. Modulus ")
    print("6. Exponentiation ")
    print("7. Floor Division ")
    
    operation = int(input("Enter your choice: "))

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = 0

    if operation == 1:
        result = num1 + num2
    elif operation == 2:
        result = num1 - num2
    elif operation == 3:
        result = num1 * num2
    elif operation == 4:
        result = num1 / num2
    elif operation == 5:
        result = num1 % num2
    elif operation == 6:
        result = num1 ** num2
    elif operation == 7:
        result = num1 // num2
    else:
        print("Invalid choice seleted.")
        return

    print("Result: " + str(result))


calculator()
