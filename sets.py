# Creating a Set

fruits = {"Apple", "Banana", "Mango", "Orange"}

print("Fruits:", fruits)


# Adding an Element

fruits.add("Grapes")
print("After adding:", fruits)


# Removing an Element

fruits.remove("Banana")
print("After removing:", fruits)


# Duplicate Values

numbers = {1, 2, 3, 3, 4, 4, 5}

print("Set removes duplicates:", numbers)


# Set Operations

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference:", set_a - set_b)
print("Symmetric Difference:", set_a ^ set_b)


# Checking an Element

if "Mango" in fruits:
    print("Mango is present")


# Loop Through a Set

for fruit in fruits:
    print("Fruit:", fruit)
