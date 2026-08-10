# Creating a List

fruits = ["Apple", "Banana", "Mango", "Orange"]

print("Fruits:", fruits)


# Accessing Elements

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# Adding Elements

fruits.append("Grapes")
print("After append:", fruits)


# Inserting an Element

fruits.insert(1, "Pineapple")
print("After insert:", fruits)


# Removing an Element

fruits.remove("Banana")
print("After remove:", fruits)


# Updating an Element

fruits[0] = "Watermelon"
print("After update:", fruits)


# List Slicing

print("First three fruits:", fruits[:3])


# Sorting

numbers = [5, 2, 8, 1, 9, 3]

numbers.sort()
print("Sorted numbers:", numbers)

numbers.reverse()
print("Reversed numbers:", numbers)


# Loop Through a List

for fruit in fruits:
    print("Fruit:", fruit)


# Find Length

print("Number of fruits:", len(fruits))
