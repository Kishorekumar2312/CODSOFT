def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

print("Please select operation -\n" "1. Add\n" "2. Subtract\n" "3. Multiply\n" "4. Divide\n")

sel = int(input("Select operation (1-4): "))
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if sel == 1:
    print(n1, "+", n2, "=", add(n1, n2))
elif sel == 2:
    print(n1, "-", n2, "=", subtract(n1, n2))
elif sel == 3:
    print(n1, "*", n2, "=", multiply(n1, n2))
elif sel == 4:
    print(n1, "/", n2, "=", divide(n1, n2))
else:
    print("Invalid input")   