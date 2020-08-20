import random
my_random_number = random.randint(1, 10)
user_guess = int(input("Guess a number between 1 - 10! "))
while user_guess != my_random_number:
    if user_guess < my_random_number:
        user_guess = int(input("That's a little low. Guess again? "))
    else:
        user_guess = int(input("That's a little high. Guess again? "))
print("You're right!")