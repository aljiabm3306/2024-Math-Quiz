import random


# Loop to check user enters yes / no
def yes_no(question):
    while True:
        response = input(question).lower()

        # checks users enter yes (Y) or no (N)
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("You did not chose a valid response")

# Generate two random numbers between 1 and 100

"""Generate a random math question."""
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
operator = random.choice(['+', '-',])
question = f"What is {num1} {operator} {num2}? "
if operator == '+':
    answer = num1 + num2
elif operator == '-':
    answer = num1 - num2

else:
    # Ensure division results in an integer
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question = f"What is {num1*num2} / {num1}? "
    answer = num2





