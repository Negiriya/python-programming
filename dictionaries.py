# Creating a Dictionary

student = {
    "name": "Riya",
    "age": 23,
    "course": "B.Tech AI & ML",
    "cgpa": 8.0
}

print("Student:", student)


# Accessing Values

print("Name:", student["name"])
print("Course:", student["course"])


# Using get()

print("Age:", student.get("age"))


# Adding a New Key-Value Pair

student["city"] = "Kashipur"

print("After adding city:", student)


# Updating a Value

student["age"] = 24

print("Updated age:", student)


# Removing a Key-Value Pair

student.pop("city")

print("After removing city:", student)


# Dictionary Keys and Values

print("Keys:", student.keys())
print("Values:", student.values())


# Loop Through Dictionary

for key, value in student.items():
    print(key, ":", value)


# Checking if a Key Exists

if "name" in student:
    print("Name exists in the dictionary")
