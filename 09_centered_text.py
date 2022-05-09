def instructions():
        # Greets the player  
        greeting = "INSTRUCTIONS"
        sides = "*" * 3
        txt = greeting
        new_str = txt.center(75)
        greeting = "{} {} {}".format(sides, greeting, sides)

        top_bottom = "*" * len(greeting)

        print("                           ",top_bottom)
        print(new_str)
        print("                           ",top_bottom)
        print()
        print("You will be asked to chose which times tables you want to practice between 2 - 1000.")
        print()
        print("You will also be asked the lowest and highest number you want timesed by with a limit of 2 - 1000.")
        print()
        print("Than it'll ask you a series of questions of the number of your choice times 2 - 1000.")
        print()
        print()
        return""