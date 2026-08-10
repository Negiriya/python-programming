# FOR LOOP

print("Numbers from 1 to 10:")

for i in range(1, 11):
    print(i)


# SUM OF NUMBERS

total = 0

for i in range(1, 11):
    total += i

print("Sum from 1 to 10:", total)


# MULTIPLICATION TABLE

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# WHILE LOOP

count = 1

while count <= 5:
    print("Count:", count)
    count += 1
