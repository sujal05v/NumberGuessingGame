import random

computer_choice = random.randint(1, 100)    #randint is a function from Python’s built-in random module.It generates a random integer (whole number) between two numbers.

user_choice = int(input("Guess the number (1-100): "))

if computer_choice == user_choice:
    print("Correct!")
elif user_choice < computer_choice:
    print("Too low!")
else:
    print("Too high!")

print("The number was:", computer_choice)