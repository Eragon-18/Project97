import random 

print("Number Guessing Game")
number = random.randint(1,9)

chances = 5

while chances > 0:
    guess = int(input("Give your guess"))
    if(guess == number):
        print("You Win")
        chances = 0
    elif(guess < number):
        print("Your guess is lower than the number")
    else:
        print("Your guess is higher than the number")
    chances = chances - 1

if(chances == 0):
    print("Game over")