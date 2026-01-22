import random

def number_guessing_game():
    print("Welcome to the guess the number game!")
    guess_number = input("Make a guess: ")
    attempts = 0

    while True:
        attempts += 1
        if guess_number.isdigit():
            guess_number = int(guess_number)
        else:
            print("Please enter a valid number!")
            continue
        
        select_number = random.randrange(0, guess_number)

        if guess_number < select_number:
            print("You are below the number.")
        elif guess_number > select_number:
            print("You are above the number.")
        else:
            print(f"Congratulations! You guessed the number {select_number} correctly in {attempts} attempts.")
            break

number_guessing_game()
