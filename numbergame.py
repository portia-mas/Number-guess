import random

def guess_game():
    # Generates a random integer
    secret_num = random.randint(1, 200)
    # print(secret_num)

    while True:
        user_input = int(input("Enter your guess: "))

        if secret_num > user_input:
            print("Guess a higher number") # guess a higher number

        elif secret_num < user_input:
            print("Guess a lower number") # guess a lower number

        elif user_input == secret_num:
            print("Correct!")  
            print(f"Guess is {secret_num}")
            break

guess_game()