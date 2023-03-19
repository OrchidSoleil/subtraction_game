import random


def intro():
    print(f"Hello! Let's challenge your subtraction skills!\n")
    print(f"Modes:\n1. Natural numbers.\n2. Rational numbers.\n3. Quit")
    print(f"Choose mode and press Enter.")

    while True:
        mode = input()
        if mode == '1':
            print("Natural Numbers subtraction.\nTo quit type 100.")
            return subtraction('1')
        elif mode == '2':
            print("Rational Numbers subtraction.\nTo quit type 100.")
            return subtraction('2')
        elif mode == '3':
            print('Bye!')
            break
        else:
            print('Please try again!')
            continue


def score(right_points, wrong_points, correct_answers):
    print(f"-----------\nYour Score:\n  Correct answers: {right_points}\n"
          f"  Wrong answers: {wrong_points}")
    for i in 'Correct answers:':
        print('-', end='')
    print("\nCorrect answers:")
    for answer in correct_answers:
        print(answer)


def subtraction(mode):
    game_on = True
    counter_rights = 0
    counter_wrongs = 0
    correct_answers = []

    while game_on:
        number1 = random.randint(20, 40)
        number2 = random.randint(10, 40 if mode == '2' else number1)
        try:
            answer = int(input(f"{number1} - {number2} = "))
            check = number1 - number2

            if answer == 100:
                print("Bye!")
                # print(correct_answers)
                game_on = False
                score(counter_rights, counter_wrongs, correct_answers)
            elif answer == check:
                counter_rights += 1
                print("Right!")
            else:
                counter_wrongs += 1
                correct_answers.append(f"{number1} - {number2} = {check}")
                print("Wrong!")
        except ValueError:
            print("Please type numbers!")


intro()
