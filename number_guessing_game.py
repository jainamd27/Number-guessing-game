import math
import random

print("Welcome to number guessing game by Jainam doshi")
lower_value = int(input("Enter the lower value:\n"))
upper_value = int(input("Enter the upper value:\n"))

# assume that the random number is x
x = random.randint(lower_value, upper_value)

# counting starts from 0
count = 0

print(f"You have {round(math.log(upper_value-lower_value+1,2))} chances to guess the right number\n")

while count < math.log(upper_value-lower_value+1,2):
    count += 1

    guess = int(input("enter the number you guessed:\n"))

    if guess == x:
        print("Congratulations! you guessed the right number\n")
        print(f"the number was {x}\n")
        print(f"You guessed the right number in {count} chances")
        break

    elif guess < x:
        print("You guessed smaller number\n")
        print("Try again!\n")
        print(f"you have wasted {count} chances\n")

    elif guess > x:
        print("You guessed bigger number\n")
        print("Try again!\n")
        print(f"You have wasted {count} chances\n")

if count > math.log(upper_value-lower_value+1, 2):
    print("You lose!\n")
    print(f"the number was {x}\n")
    print("Better luck next time!")