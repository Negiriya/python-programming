# Basic Exception Handling

try:
    number = int(input("Enter a number: "))
    print("You entered:", number)

except ValueError:
    print("Please enter a valid number.")


# Handling Division by Zero

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid numbers.")


# try-except-else-finally

try:
    number = int(input("Enter a number: "))

except ValueError:
    print("Invalid input.")

else:
    print("Valid number:", number)

finally:
    print("Program execution completed.")
