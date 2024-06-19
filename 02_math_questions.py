import random


# checking user enters yes / no (takes in a question)
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")

    response = input(question).lower()
    # checks user response, question
    # repeats if users don't enter yes / no
    if response == "yes" or response == "y":
        return "yes"
    elif response == "no" or response == "n":
        return "no"
    else:
        print("Please enter yes / no")


def instructions():
    print('''
    
**** instructions ****

To begin the maths quiz, choose the amount of questions
you would like to answer 

Good Luck!

    ''')


# generate two numbers
num1 = random.randint (1,90)
num2 = random.randint (1,90)
# main rotine
print()
# make them into a question
equation = f"{num1} + {num2}"
# ask the user the question.
print(equation)
correct_answer = num1 + num2





