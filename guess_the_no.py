import random
target = random.randint(1, 100)
while True:
    userChoice = int(input("Guess the target: "))
    if userChoice == target:
        print("Congratulations! You've guessed the correct number.")
        break
    elif (userChoice < target):
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
        continue
