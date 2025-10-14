while True:

    test = input("Continue? [y/n]: ")
    if test == "y":
        enter = int(input("Enter a number: "))
        if enter % 2 == 0:
            print(f"{enter} is an even number")
        else:
            print(f"{enter} is an odd number")
    else:
        break

# --------------------------------------------------

enter_1 = str(input("Enter string: "))
enter_2 = input("What letter should we count?: ")
print(f"There are", enter_1.count(enter_2), enter_2, "'s", "in the string.")
test = 0
for letter in enter_1:
    if letter == enter_2:
        test += 1
print("There are", test, enter_2, "'s", "in the string.")

# --------------------------------------------------

count = 0
while True:
    if count == 3:
        break
    count += 1
    print(count)

# --------------------------------------------------

count = 1
while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

# --------------------------------------------------

for i in range(1, 11):
    print(i)

# --------------------------------------------------

value1 = 1
value2 = 1
while value1 <= 2:
    print("value1", value1)
    while value2 <= 5:
        print("value2", value2)
        value2 += 1
    value2 = 1
    value1 += 1

# --------------------------------------------------

i = 1
while i <= 4:
    j = 0
    while j <= 3:
        print(i*j, end=" ")
        j += 1
        print()
        i += 1

# First 1*0=0 2*1=2 3*2=6 4*3=12 it stops at 4*3=12 because it satisfies both while loops 4 and 3


# --------------------------------------------------

while True:
    print(" 1. Addition\n 2. Subtraction\n 3. Multiplication\n 4. Division\n 5. Exit")
    user = input("Choose operation: ")
    if user == "1":
        first = int(input("Enter first operand: "))
        second = int(input("Enter second operand: "))
        print(f"Sum:", first + second)
    elif user == "2":
        first = int(input("Enter first operand: "))
        second = int(input("Enter second operand: "))
        print(f"Difference:", first - second)
    elif user == "3":
        first = int(input("Enter first operand: "))
        second = int(input("Enter second operand: "))
        print(f"Product:", first * second)
    elif user == "4":
        first = int(input("Enter first operand: "))
        second = int(input("Enter second operand: "))
        print(f"Quotient:", first / second)
    else:
        exit()

# --------------------------------------------------

test = "test number 2"
result = test.split(" ")
"print(len(result))"
for i in result:
    print(i)

# --------------------------------------------------

name = str(input("Enter Name: "))
age = int(input("Enter Age: "))
print(f"Your name is {name} and age is {age}")
print("Your name is %s and age is %d" % (name, age)) # %s means string and %d means digit

print(name.isalpha()) 
