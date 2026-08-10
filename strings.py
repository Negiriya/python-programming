# String Basics

text = "Python Programming"

print("String:", text)
print("Length:", len(text))


# Indexing

print("First character:", text[0])
print("Last character:", text[-1])


# Slicing

print("First 6 characters:", text[:6])
print("Last 11 characters:", text[7:])


# String Methods

name = "riya negi"

print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", name.title())


# Replace

message = "I am learning Java"

print("Updated message:", message.replace("Java", "Python"))


# Check whether a word exists

sentence = "Python is easy to learn"

print("Python" in sentence)


# Reverse a String

word = "hello"

print("Reverse:", word[::-1])


# Palindrome Check

word = input("Enter a word: ")

if word == word[::-1]:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")
