answer=5
guess=int(input("Please enter the number between 1 and 10:"))

if guess !=answer:
    if guess<answer:
        print("Guess Higher")
    else:
        print("Please guess lower")
    guess=int(input("Please enter your guess: "))
    if guess==answer:
        print("Well done, you guessed it")
    else:
        print("you have guessed it wrong")
else:
    print("you got it first time")
# if guess<answer:
#     print("Please guess higher")
#     guess=int(input("Please enter your guess: "))
#     if guess==answer:
#         print("Well done, you guessed it correct")
#     else:
#         print("Sorry, you have guessed it wrong")
# elif guess>answer:
#     print("Please guess lower")
#     guess=int(input("Please enter your guess: "))
#     if guess==answer:
#         print("Well done, you guessed it correct")
#     else:
#         print("Sorry, you have guessed it wrong")
# else:
#     print("you got it first time")