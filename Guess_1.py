answer=5
guess=int(input("Please enter the number between 1 and 10:"))

if guess ==answer:
    print("you got it first time")
else:
    if guess<answer:
        print("Guess Higher")
    else:
        print("Please guess lower")
    guess=int(input("Please enter your guess: "))
    if guess==answer:
        print("Well done, you guessed it")
    else:
        print("you have guessed it wrong")

