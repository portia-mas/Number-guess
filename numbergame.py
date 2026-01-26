import random

def guess_game():
    # Generates a random integer
    secret_num = random.randint(1, 100)
    # print(secret_num)
    print("Guess a number between 1-100")
    while True:
        user_input = int(input("\nEnter your guess: "))

        if secret_num > user_input:
            print("\nGuess a higher number") # guess a higher number

        elif secret_num < user_input:
            print("\nGuess a lower number") # guess a lower number

        elif user_input == secret_num:
            print("\nCorrect!")  
            print(f"Guess is {secret_num}")
            break

guess_game()