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

# Lists of valid responses 
yes_no_list = ["yes", "no"]
yes_no_error = "Please answer yes or no"

rounds_played = 0
rounds_lost = 0
rounds_won = 0

# Above is there so there's no errors


print()
user_history = choice_checker("Would you like to see your game history? ", yes_no_list, yes_no_error)
if user_history == "yes":
    
    rounds_won = rounds_played - rounds_lost


# If 'yes' show game history

# RPS Component 6 - Scoring System
game_summary = []

# Rounds won will be calculated (total - draw - lost)


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