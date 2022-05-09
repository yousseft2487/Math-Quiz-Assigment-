
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


# Main routine goes here 
statement_generator("Welcome to the Lucky Unicorn Game", "*", 3)
print()
statement_generator("Congratulations you got a Unicorn", "!", 1)    