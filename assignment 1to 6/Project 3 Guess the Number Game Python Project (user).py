import random

def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")
    
    low = 1
    high = 100
    attempts = 0
    
    while True:
        attempts += 1
        guess = random.randint(low, high)
        print(f"Is your number {guess}?")
        
        feedback = input("Enter 'h' if the guess is too high, 'l' if the guess is too low, or 'c' if I guessed it correctly: ").lower()
        
        if feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input, please enter 'h', 'l', or 'c'.")

# Start the game
guess_the_number()
