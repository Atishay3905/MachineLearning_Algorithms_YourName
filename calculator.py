# Simple Calculator 🧮

print("Welcome to the Simple Calculator!")

# Get user input
num1 = float(input("Enter the first number: "))
operator = input("Choose an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation
if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("⚠️ Cannot divide by zero!")
else:
    print("❌ Invalid operator!")
