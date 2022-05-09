import random

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

comp_equation = 0
secret = random.randint(2, 12)

# Have comp loop +1 everytime user gets answer right

# Asks user what times tables they want to learn
user_choice = "What times tables do you want to learn?"
if user_choice == 2:
    comp_equation = 2 * 2
print("")






