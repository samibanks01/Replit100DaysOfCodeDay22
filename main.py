print("Totally Random One-Million-to-One")

print()

import random

myNumber = random.randint(1, 1000000)
counter = 0
while True:
  guess = int(input("What is your guess?: "))
  if guess < myNumber:
    print("Too low")
    counter += 1
  elif guess > myNumber:
    print("Too high")
    counter += 1
  elif guess == myNumber:
    print("Correct!")
    counter += 1
    break
  else:
    print("That is not a number I recognize.")

print("It took you", counter, "guesses to get the number correct.")
print("Click 'run' to try again with a different number.")

