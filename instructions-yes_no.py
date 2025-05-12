while True:

    Yes = ("yes", "y")
    No = ("no", "n")

    Question = input("Will you move on to the next project?")

    if Question.lower() in Yes:
        continue

    elif Question.lower() in No:
        continue

    else:
        print("Please enter yes or no.")
