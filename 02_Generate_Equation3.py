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

user_choice = int_check("What times tables do you want to learn ? ") # replace with fncn in due course

for comp_choice in range(2, 12 + 1):
# comp_choice = 2 
    comp_equation = comp_choice * user_choice
    user_answer = int(input("What is {} x {} ? ".format(comp_choice, user_choice)))
    if user_answer == comp_equation:
        print("Congratulations you got it right.")
        comp_choice += 1
    else:
        print("You got it wrong, the answer is {}".format(comp_equation))






    