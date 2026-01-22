# Experiment 2
# Calculator program 

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b


while True:
    print("\nSimple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")

    choice = int(input("Enter your choice (1-6): "))

    if choice < 1 or choice > 6:
        print("Invalid choice")
    else:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", add(num1, num2))

        elif choice == 2:
            print("Result:", subtract(num1, num2))

        elif choice == 3:
            print("Result:", multiply(num1, num2))

        elif choice == 4:
            if num2 == 0:
                print("Division by zero is not allowed")
            else:
                print("Result:", divide(num1, num2))

        elif choice == 5:
            print("Result:", modulus(num1, num2))

        elif choice == 6:
            print("Result:", power(num1, num2))

    cont = input("wanna continue? (yes/no): ")
    if cont != "yes":
        print("Program terminated")
        break
