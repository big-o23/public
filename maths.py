from random import randint
#Created by Owen Schmierer 17/8/2020
#For my gorgeous kids
#To do - add a timer, and summary output to a list.

def multiply(num1, num2):
    global correct_count, total_count

    quiz1 = int(num1) * int(num2)
    #print(f"{num1} * {num2} = {quiz1}") #This prints the answer.

    while True:
        print(f"What is {num1} X {num2}")
        answer = input("> ")
        try:
            answer = int(answer)
        except:
            print('Please use numeric digits')
            continue
        break


    if int(answer) == int(quiz1):
        print("You got it correct!")
        correct_count += 1
    else:
        print(f"Try the next question.  The answer is {int(quiz1)}.")
    total_count += 1

def divide(num1, num2):
    global correct_count, total_count

    #Do a multiply
    quiz1 = int(num1) * int(num2)
    #Use the multiplication to get division question to avoid fractions
    quiz4 = int(quiz1) / int(num1) #quiz4 = num2


    #print(f"{num1} * {num2} = {quiz1}") #This prints the answer.
    while True:
        print(f"What is {quiz1} / {num1}")
        answer = input("> ")
        try:
            answer = int(answer)
        except:
            print('Please use numeric digits')
            continue
        break

    if int(answer) == int(quiz4):
        print("You got it correct!")
        correct_count += 1
    else:
        print(f"Try the next question.  The answer is {int(quiz4)}.")
    total_count += 1

def addition(num1, num2):
    global correct_count, total_count

    quiz2 = int(num1) + int(num2)
    while True:
        print(f"What is {num1} + {num2}")
        answer = input("> ")
        try:
            answer = int(answer)
        except:
            print('Please use numeric digits')
            continue

        break

    if int(answer) == int(quiz2):
        print("You got it correct!")
        correct_count += 1
    else:
        print(f"Try the next question.  The answer is {int(quiz2)}.")
    total_count += 1

def subtraction(num1, num2):
    global correct_count, total_count

    quiz3 = int(num1) - int(num2)

    while True:
        print(f"What is {num1} - {num2}")
        answer = input("> ")
        try:
            answer = int(answer)
        except:
            print('Please enter numeric digits.')
            continue
        break

    if int(answer) == int(quiz3):
        print("You got it correct!")
        correct_count += 1
    else:
        print(f"Try the next question.  The answer is {int(quiz3)}")
    total_count += 1

correct_count = int(0)
total_count = int(0)

print("Would you like 1) multiply, 2) addition 3) subtraction 4) division")
type = input("> ")

######## MULTIPLICATION
if int(type) == 1:
    while True:
        while True:
            print("Would you like 1) random numbers, or 2) to suggest a number?")
            query1 = input("> ")
            try:
                query1 = int(query1)
            except:
                print('Please enter 1 or 2')
                continue
            break

        if int(query1) == 1:
            i = 1
            while i <= 20:
                randomnum1 = f"{randint(1,12)}"
                randomnum2 = f"{randint(1,12)}"
                multiply(randomnum1, randomnum2)
                i += 1
                print(f"You have {correct_count} correct out of {total_count} total.")
        elif int(query1) == 2:
            print("What number would you like?")
            choosenumber = input("> ")
            i = 1
            while i <= 20:
                randomnum2 = f"{randint(1,12)}"
                multiply(choosenumber, randomnum2)
                i += 1
                print(f"You have {correct_count} correct out of {total_count} total.")

#################################### ADDITION
elif int(type) == 2:
    i = 1
    while i <= 10:
        randomnum3 = f"{randint(10,100)}"
        randomnum4 = f"{randint(10,100)}"
        addition(randomnum3, randomnum4)
        i += 1
        print(f"You have {correct_count} correct out of {total_count} total.")

####################################################SUBTRACTION
elif int(type) == 3:
    i = 1
    while i <= 10:
        randomnum5 = f"{randint(10,100)}"
        randomnum6 = f"{randint(10,100)}"
        #Set variables to work out which number is the biggest, to subtract from.
        if int(randomnum5) >= int(randomnum6):
            sub_big = int(randomnum5)
            sub_little = int(randomnum6)
        else:
            sub_big = int(randomnum6)
            sub_little = int(randomnum5)
        subtraction(sub_big, sub_little)
        #print(f"sub_big={sub_big}")
        #print(f"sub_little={sub_little}")
        i += 1
        print(f"You have {correct_count} correct out of {total_count} total.")

####################DIVISION
elif int(type) == 4:
    while True:
        while True:

            print("Would you like 1) random numbers, or 2) to suggest a number?")
            query1 = input("> ")
            try:
                query1 = int(query1)
            except:
                print('Enter 1 or 2 please')
                continue
            break

        if int(query1) == 1:
            i = 1
            while i <= 20:
                randomnum7 = f"{randint(1,12)}"
                randomnum8 = f"{randint(1,12)}"
                divide(randomnum7, randomnum8)
                i += 1
                print(f"You have {correct_count} correct out of {total_count} total.")

        elif int(query1) == 2:
            print("What number would you like?")
            choosenumber = input("> ")
            i = 1
            while i <= 20:
                randomnum2 = f"{randint(1,12)}"
                divide(choosenumber, randomnum2)
                i += 1
                print(f"You have {correct_count} correct out of {total_count} total.")
