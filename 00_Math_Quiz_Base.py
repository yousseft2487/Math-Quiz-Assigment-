import random

# Functions go here
def check_rounds():
    while True:
        response = input("How many rounds: ")

        round_error = "Please type either <enter> or an integer that is more than 0\n"

        # If infinite mode not chosen, check response is an integer that is more than 0
        if response != "":
            try:
                response = int(response)

                # If response is too low, go back to start of loop
                if response < 1:
                    print(round_error)
                    continue

            except ValueError:
                print(round_error)
                continue

        return response


def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # interates through list and if response is an item
        # in the list (or the first letter of an item), the full item 
        # name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


def instructions():
        print()
        print("You will be asked to chose which times tables you want to practice between 2 - 12.")
        print()
        print("Than it'll ask you a series of questions of the number of your choice times 1 - 12.")
        print()
        print("If you want to do it more than once without restarting the program you can chose to do more than 1 round or enter for continuous mode.")
        print()
        return""


# makes the text look better, adds to the austhetics 
def statement_generator(statement, decoration, lines):

    sides = decoration * 3
    statement = "{} {} {}".format(sides, statement, sides)
    
    if lines == 1:
        print(statement)
    else:
        top_bottom = decoration * len(statement)

        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""

def int_check(question, low=2, high=12):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < 2 or response > 12:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

        # checks input is a integer 
        except ValueError:
            print("Please enter an integer")
            continue

            

# Main routine goes here


# Lists of valid responses 
yes_no_list = ["yes", "no"]
yes_no_error = "Please answer yes or no"



# ask user for # of rounds then loop...
game_summary = []

rounds_played = 0

# intialise lost / drawn counters
rounds_lost = 0
rounds_won = 0
num_won = 0 


# Greets the player  
greeting = "Hello, and welcome to the Multiplaction Quizz."
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)

# ask user if they want to see instructions 
# If 'yes', show instructions
want_instructions = choice_checker("Do you want to see the instructions? ", yes_no_list, yes_no_error)

if want_instructions == "yes":
    instructions()

print()




# Ask  user for # of rounds, <enter> for infinite mode
rounds = check_rounds()


end_game = ""
while end_game == "":

    # Start of Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Rounds {} (xxx to quit)".format(rounds_played + 1)
    else:
        heading = "Rounds {} of {}".format(rounds_played +1, rounds)

    print(heading)

    # generate secret number

    # loop to ask user to guess number
       # Number Checking function goes here
    

    
user_choice = int(input("What times tables do you want to learn ? ")) # replace with fncn in due course

for comp_choice in range(2, 12 + 1):
# comp_choice = 2 
    comp_equation = comp_choice * user_choice
    user_answer = int(input("What is {} x {} ? ".format(comp_choice, user_choice)))
    if user_answer == comp_equation:
        print("Congratulations you got it right.")
        comp_choice += 1
        rounds_won += 1
    else:
        print("You got it wrong, the answer is {}".format(comp_equation))
        rounds_lost += 1






    
            
   

    rounds_played += 1

    # in infinite mode, ask user if they wish to continue
    if rounds == "":
        end_game = input("Press <enter> for another round or any key to quit ")

    # Ask user if they want to see their game history.
    if end_game != "" or rounds_played == rounds:
        break

print()
user_history = choice_checker("Would you like to see your game history? ", yes_no_list, yes_no_error)
if user_history == "yes":
    
    rounds_won = rounds_played - rounds_lost


# If 'yes' show game history


# Show game statistics
# **** Calculate Game Stats ******
    percent_win = (rounds_won / rounds_played) * 100
    percent_lose = (rounds_lost / rounds_played) * 100

    print()
    print("***** Game History *******")
    for game in game_summary:
        print(game)

    print()

    # displays game stats with % values to the nearest whole number
    print("******* Game Statistics *******")
    print("Correct: {}, ({:.0f}%) ".format(rounds_won, percent_win))
    print("Incorrect: {}, ({:.0f}%) ".format(rounds_lost, percent_lose))
            

    # End of Game Statements 
    print()
    print('***** End Game Summary *****')
    print("Correct: {} \t|\t Incorrect:{} ".format(rounds_won, rounds_lost))

print()
print("***** Thanks for playing *****")

