import random

# Functions go here



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
    
# Greets the player  
greeting = "Hello, and welcome to the Multiplaction Quizz."
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)


def instructions():
        # Greets the player  
        greeting = "INSTRUCTIONS"
        sides = "*" * 3

        greeting = "{} {} {}".format(sides, greeting, sides)

        top_bottom = "*" * len(greeting)

        print(top_bottom)
        print(greeting)
        print(top_bottom)
        print()
        print("You will be asked to chose which times tables you want to practice between 2 - 1000.")
        print()
        print("You will also be asked the lowest and highest number you want timesed by with a limit of 2 - 1000.")
        print()
        print("Than it'll ask you a series of questions of the number of your choice times 2 - 1000.")
        print()
        print()
        return""


# makes the text look better, adds to the austhetics 

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
        return response 

def int_check2(question, low=2, high=1000):

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
                if response < 2 or response > 1000:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

        # checks input is a integer 
        except ValueError:
            print("Please enter an integer")
            continue
        return response 

def int_check3(question, low=2, high=1000):

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
                if response < 2 or response > 1000:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

        # checks input is a integer 
        except ValueError:
            print("Please enter an integer")
            continue
        return response 

            

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

play_again = 0 



# ask user if they want to see instructions 
# If 'yes', show instructions
want_instructions = choice_checker("Do you want to see the instructions? ", yes_no_list, yes_no_error)

if want_instructions == "yes":
    instructions()

print()

# Asks user lowest and highest numbers the want timesed by
lowest = int_check3("Lowest Number: ")
highest = int_check3("Highest Number: ", lowest +1)


# Ask  user for # of rounds, <enter> for infinite mode


end_game = ""

 # Start of Game Play Loop
  

    
user_choice = int_check3("What times tables do you want to learn ? ") # replace with fncn in due course

for comp_choice in range(lowest, highest + 1):
# comp_choice = 2 
    comp_equation = comp_choice * user_choice
    user_answer = input("What is {} x {} ? ".format(comp_choice, user_choice))
    if user_answer == comp_equation:
        print("Congratulations you got it right.")
        comp_choice += 1
        rounds_won += 1
    else:
        print("You got it wrong, the answer is {}".format(comp_equation))
        rounds_lost += 1



    rounds_played += 1

    # in infinite mode, ask user if they wish to continue

    # Ask user if they want to see their game history.
    if end_game != "" or rounds_played == 12:
        break

print()
user_history = choice_checker("Would you like to see your game history? ", yes_no_list, yes_no_error)
if user_history == "yes":
    
    rounds_won = rounds_played - rounds_lost


# If 'yes' show game history
    for item in range(lowest, highest):
        result = input("choose result: ")

        outcome = "Round {}: {}".format(item, result)

        if result == "Lost":
            rounds_lost += 1

        game_summary.append(outcome)

    rounds_won = rounds_played - rounds_lost 

# Show game statistics
# **** Calculate Game Stats ******
    percent_win = (rounds_won / rounds_played) * 100
    percent_lose = (rounds_lost / rounds_played) * 100

    print()


    # displays game stats with % values to the nearest whole number
    print("******* Quiz Statistics *******")
    print("Correct: {}, ({:.0f}%) ".format(rounds_won, percent_win))
    print("Incorrect: {}, ({:.0f}%) ".format(rounds_lost, percent_lose))
            

    # End of Game Statements 
    print()
    print('***** End Quiz Summary *****')
    print("Correct: {} \t|\t Incorrect:{} ".format(rounds_won, rounds_lost))

print()
print("***** Thanks for playing *****")

