def mad_libs():
    print("Welcome to Mad Libs!")
    print("Please provide the following words:")

    noun1 = input("Enter a noun: ")
    adjective1 = input("Enter an adjective: ")
    verb1 = input("Enter a verb (past tense): ")
    noun2 = input("Enter another noun: ")
    place = input("Enter a place: ")
    verb2 = input("Enter a verb: ")
    adjective2 = input("Enter another adjective: ")

    story = f"""
    One day, a {adjective1} {noun1} decided to {verb1} to {place}.
    On the way, it saw a {adjective2} {noun2} and couldn't resist but {verb2} it!
    It was a day to remember.
    """

    print("\nHere is your Mad Libs story:\n")
    print(story)

mad_libs()
