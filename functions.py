# Simple Function

def greet():
    print("Hello, Riya!")


greet()


# Function with Parameters

def greet_user(name):
    print("Hello,", name)


greet_user("Riya")


# Function with Return Value

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print("Sum:", result)


# Find the Greatest of Two Numbers

def greatest(a, b):
    if a > b:
        return a
    else:
        return b


print("Greatest:", greatest(15, 25))


# Check Even or Odd

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(check_even_odd(10))
print(check_even_odd(7))
