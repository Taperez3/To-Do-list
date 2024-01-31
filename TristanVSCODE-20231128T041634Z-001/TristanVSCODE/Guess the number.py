# Tristan Perez
# Guess the Number
import random

# Function
def guess_the_number():
    # this line makes a random number between 1 and 10
    secret_number = random.randint(1, 10)
    
    # the user enter their first guess
    user_guess = int(input("Guess the number between 1 and 10: "))
    
    # Checks if the user guess is right
    if user_guess == secret_number:
        print("Congratulations! You got the right number.!!!")
    else:
        # Prints the right number, and tells the user that they lost
        print("Sorry you lost. The correct number was " + str(secret_number) + ".")

# Main
guess_the_number()
