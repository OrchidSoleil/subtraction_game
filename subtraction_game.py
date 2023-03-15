import random


def intro():
    print(f"Hello! Let's challenge your subtraction skills!\n")
    print(f"Modes:\n1. Natural numbers.\n2. Negative numbers.\n3. Quit")
    print(f"Choose mode and press Enter.")

    while True:
        mode = input()
        if mode == '1':
            return natural_numbers()
        elif mode == '2':
            return rational_numbers()
        elif mode == '3':
            print('Bye!')
            break
        else:
            print('Please try again!')
            continue


def natural_numbers():
    print("Natural Numbers subtraction.\nTo quit type 100.")
    game_on = True
    counter_rights = 0
    counter_wrongs = 0

    while game_on:
        number1 = random.randint(20, 40)
        number2 = random.randint(0, number1)
        try:
            answer = int(input(f"{number1} - {number2} = "))
            check = number1 - number2

            if answer == 100:
                print("Bye!")
                game_on = False
                # score(counter_rights, counter_wrongs)
            elif answer == check:
                counter_rights += 1
                print("Right!")
            else:
                counter_wrongs += 1
                print("Wrong!")
        except ValueError:
            print("Please type numbers!")


def rational_numbers():
    print("Rational Numbers subtraction.\nTo quit type 100.")
    game_on = True
    counter_rights = 0
    counter_wrongs = 0

    while game_on:
        number1 = random.randint(20, 40)
        number2 = random.randint(0, 30)
        try:
            answer = int(input(f"{number1} - {number2} = "))
            check = number1 - number2

            if answer == 100:
                print("Bye!")
                # score(counter_rights, counter_wrongs)
                game_on = False
            elif answer == check:
                counter_rights += 1
                print("Right!")
            else:
                counter_wrongs += 1
                print("Wrong!")
        except ValueError:
            print("Please type numbers!")


intro()
