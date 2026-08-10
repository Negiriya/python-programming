# Writing to a File

file = open("example.txt", "w")
file.write("Hello, I am learning Python!")
file.close()


# Reading from a File

file = open("example.txt", "r")
content = file.read()
print("File content:", content)
file.close()


# Appending to a File

file = open("example.txt", "a")
file.write("\nI am also learning DSA.")
file.close()


# Reading Line by Line

file = open("example.txt", "r")

for line in file:
    print(line.strip())

file.close()


# Using with Statement

with open("example.txt", "r") as file:
    content = file.read()
    print("Final content:")
    print(content)
