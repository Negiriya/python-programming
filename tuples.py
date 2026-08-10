# Creating a Tuple

fruits = ("Apple", "Banana", "Mango", "Orange")

print("Fruits:", fruits)


# Accessing Elements

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


# Tuple Length

print("Number of fruits:", len(fruits))


# Tuple Slicing

print("First two fruits:", fruits[:2])


# Loop Through a Tuple

for fruit in fruits:
    print("Fruit:", fruit)


# Checking an Element

if "Mango" in fruits:
    print("Mango is present")


# Tuple with Different Data Types

student = ("Riya", 23, "B.Tech AI & ML", 8.0)

print("Student:", student)


# Tuple Unpacking

name, age, course, cgpa = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("CGPA:", cgpa)
