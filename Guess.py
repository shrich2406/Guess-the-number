from random import randint

def logic(attempt):
    guess = int(randint(1, 100))
    print(f"You have {attempt} attempts to guess the number:")
    while attempt > 0:
        num = int(input("Make a guess:"))
        if num == guess:
            print("You guessed right")
            break
        elif num > guess:
            print("Too high")
        else:
            print("Too low")
        attempt -= 1
        if attempt > 0:
            print("Guess again")
            print(f"You have {attempt} attempts remaining to guess the number")
    else:
        print(f"You have ran out of attempts.The correct number was {guess}")


while True:
    mode = input(" Type 'easy' or 'hard'")
    if mode == "easy":
        n = 10
    elif mode == "hard":
        n = 5
    else:
        n = 5
    logic(n)
    repeat = input("Do you want to play again 'yes' or 'no' :")
    if repeat != "yes":
        print("Thank you for playing!")
        break

