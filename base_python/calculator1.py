import math
def add(x, y):
    return x + y
def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x, base=math.e):
    return math.log(x, base)

def sine(x):
    return math.sin(math.radians(x))

def cosine(x):
    return math.cos(math.radians(x))

def tangent(x):
    return math.tan(math.radians(x))

def factorial(x):
    return math.factorial(x)
def show_menu():
    print("\n--- Scientific Calculator ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exponentiation")
    print("6. Square Root")
    print("7. Logarithm")
    print("8. Sine")
    print("9. Cosine")
    print("10. Tangent")
    print("11. Factorial")
    print("12. Exit")
def main():
    while True:
        show_menu()
        choice = input("Choose an operation (1-12): ")

        if choice == "1":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {add(x, y)}")

        elif choice == "2":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {subtract(x, y)}")

        elif choice == "3":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {multiply(x, y)}")

        elif choice == "4":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            print(f"Result: {divide(x, y)}")

        elif choice == "5":
            x = float(input("Enter the base: "))
            y = float(input("Enter the exponent: "))
            print(f"Result: {power(x, y)}")

        elif choice == "6":
            x = float(input("Enter the number: "))
            print(f"Result: {square_root(x)}")

        elif choice == "7":
            x = float(input("Enter the number: "))
            base = float(input("Enter the base (default is e): ") or math.e)
            print(f"Result: {logarithm(x, base)}")

        elif choice == "8":
            x = float(input("Enter the angle in degrees: "))
            print(f"Result: {sine(x)}")

        elif choice == "9":
            x = float(input("Enter the angle in degrees: "))
            print(f"Result: {cosine(x)}")

        elif choice == "10":
            x = float(input("Enter the angle in degrees: "))
            print(f"Result: {tangent(x)}")

        elif choice == "11":
            x = int(input("Enter the number: "))
            print(f"Result: {factorial(x)}")

        elif choice == "12":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
