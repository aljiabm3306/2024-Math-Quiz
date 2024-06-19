import random


# Checks for an integer more than 0 (allows <enter>)
def int_check(answer):
    error = "please enter an integer that is 1 or more."

    while True:

        response = input(question)
        if response == "":
            return "infinite"

        try:
            # response = int(input("Enter an integer: "))
            response = int(response)

            # checks that the number is more than / equal of 1
            if response > 0:
                return response

            else:
                print(error)


        except ValueError:
            print(error)


# main routine
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


num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

question = f"{num_2} + {num_1} = "

ask = int_check(question)

print("you typed in", ask)

# how we got questions
mode = "easy"
questions = 0

rounds_played = 0

rounds_win = 0
rounds_loss = 0

game_history = []

yes_no = ("yes", "no")
math_options = ("-", "+")



def instructions():
    pass


if want_instructions == "yes":
    instructions()
else:
    pass

# Main Routine
print()
print("Welcome to the maths quiz!")
print()

# loop for testing purposes

want_instructions = yes_no

# checks user enters yes (y) or no (n)
if want_instructions == "yes":
    instructions()

print("program continues")

# generate two numbers
num1 = random.randint(1, 90)
num2 = random.randint(1, 90)
# main rotine
print()
# make them into a question
equation = f"{num1} + {num2}"
# ask the user the question.
print(equation)
correct_answer = num1 + num2

ask = int_check(question)

# Ask the numbers of rounds / infinite mode
num_rounds = int_check("how many rounds you like? push <enter> for infinite mode:")

if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 6

# Game loop started here
while rounds_played < num_rounds:

    # rounds to playing
    if mode == "infinite":
        rounds_heading = f"\n rounds {rounds_played + 1} (infinite mode)"
    else:
        rounds_heading = f"\n rounds {rounds_played + 1} (infinite mode)"

    print(rounds_heading)
    print()

    user_choice = ("choose:", math_options)
    print(f"you chose {user_choice}")

    if user_choice == "xxx":
        break

    comp_choice = random.choice(math_options[:-1])

    # pauses program until user types something
    input(num_1 + num_2)

    if result == "correct":
        rounds_win += 1
        feedback = "👍👍 you won!👍👍 "
    elif result == "lose":
        rounds_loss += 1
        feedback = "😟😟 you lost.😟😟"

    # set up rounds feedback and input it user
    # how you can get the answers
    rounds_feedback = f"{user_answer} vs {comp_answer}, {feedback}"
    history_item = f"round: {rounds_played + 1} - {rounds_feedback}"

    print(rounds_feedback)
    game_history.append(history_item)

    rounds_played += 1

    # if users are in infinite mode, increase number of rounds!
    if mode == "infinite":
        num_rounds += 1

# game history / Statistics area
rounds_win = rounds_played - rounds_loss - rounds_win
percent_won = rounds_win / rounds_played * 100
percent_lost = rounds_loss / rounds_played * 100

print(f"Rounds won: {percent_won:.2f} \t"
      f"LOST: {percent_lost:.2f} \t")

# Iterates through list, outputs game history
for item in game_history:
    print(item)
