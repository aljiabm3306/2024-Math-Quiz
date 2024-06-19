import random

# Function to check for a positive integer input (allows <enter> for "infinite" mode)
def int_check(question):
    error = "Please enter an integer that is 1 or more."

    while True:
        response = input(question)

        if response == "":
            return "infinite"

        try:
            response = int(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

# Function to get yes/no answers
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please choose a valid response (yes/y or no/n)")

# Main Routine
print("Welcome to the math quiz!\n")

# Ask if the user wants instructions
want_instructions = yes_no("Would you like instructions? (yes/no): ")

# Function to display instructions
def instructions():
    print("Instructions: Answer the math questions correctly to win!")

# Display instructions if requested
if want_instructions == "yes":
    instructions()

print("Let's start the quiz!\n")

# Initialize game variables
rounds_played = 0
rounds_win = 0
rounds_loss = 0
game_history = []

# Ask for number of rounds or choose infinite mode
num_rounds = int_check("How many rounds would you like to play? Press <enter> for infinite mode: ")

# Set mode based on user input
if num_rounds == "infinite":
    mode = "infinite"
    num_rounds = 1000000000  # Default rounds if infinite mode is chosen

else:
    mode = "limited"

# Game loop
while rounds_played < num_rounds:
    rounds_played += 1

    # Generate random numbers for the math question
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2

    # Ask the user the math question
    question = f"What is {num1} + {num2}? "
    user_answer = int_check(question)

    # Compare user's answer with the correct answer
    if user_answer == correct_answer:
        rounds_win += 1
        result = "correct"
        feedback = "👍👍 correct 👍👍"
    else:
        rounds_loss += 1
        result = "lose"
        feedback = "😟😟 incorrect. 😟😟"

    # Record round history
    rounds_feedback = f"{feedback}" \
                      f" Round {rounds_played}: {question}"
    game_history.append(rounds_feedback)

    # Print round feedback
    print(rounds_feedback)

# Calculate and print game statistics
percent_won = (rounds_win / rounds_played) * 100
percent_lost = (rounds_loss / rounds_played) * 100

print(f"\nGame Statistics:")
print(f"Rounds played: {rounds_played}")
print(f"Rounds won: {rounds_win} ({percent_won:.2f}%)")
print(f"Rounds lost: {rounds_loss} ({percent_lost:.2f}%)")

# Print game history
print("\nGame History:")
for item in game_history:
    print(item)
