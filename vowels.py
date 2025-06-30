def oddeven():
    global num
    num = int(input("Enter your number: "))
    if num % 2 == 0:
        print("This number is even")
    else:
        print("This number is odd")


oddeven()


def contvowels():
    word = input("Enter a word: ")
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in word:
        if char in vowels:
            count += 1
        else:
            count += 0
    print("The number of vowels is:", count)


contvowels()


def squareroot():
    global num
    num = int(input("Enter a number: "))
    square = num ** 2
    cube = num ** 3
    print(square, cube)


squareroot()


def agefinder():
    age = int(input("What is your age: "))
    if age >= 18:
        print("You are eligible to drive")
    else:
        print("You are not eligible to drive")
    number = int(input("Enter a number: "))
    if number > 0:
        print("This is positive number")
    elif number < 0:
        print("This is negative number")
    else:
        print("This is zero")


agefinder()





