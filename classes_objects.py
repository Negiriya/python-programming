# Class and Object

class Student:

    def introduce(self):
        print("Hello, I am a student.")


# Creating an Object

student1 = Student()

student1.introduce()


# Class with Attributes

class Student:

    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)


# Creating Objects

student1 = Student("Riya", "B.Tech AI & ML")
student2 = Student("Aman", "B.Tech CSE")

student1.display()
print()

student2.display()
