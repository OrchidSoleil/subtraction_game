import random

game_on = True

while game_on:
    number1 = random.randint(20, 40)
    number2 = random.randint(10, 30)
    print("To quit press 100.")

    try:
        answer = int(input(f"{number1} - {number2} = "))
        check = number1 - number2
        if answer == 100:
            print("Bye!")
            game_on = False
        elif answer == check:
            print("Right!")
        else:
            print("Wrong!")
    except ValueError:
        print("Please use numbers!")


