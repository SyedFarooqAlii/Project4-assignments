import random

words = ['python', 'hangman', 'programming', 'developer', 'computer', 'challenge', 'algorithm', 'software']

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    print("Welcome to Hangman!")
    
    word = choose_word()
    guessed_letters = []
    attempts = 6
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts left.")
        print("Current word:", display_word(word, guessed_letters))
        
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! The letter {guess} is in the word.")
        else:
            attempts -= 1
            print(f"Oops! The letter {guess} is not in the word.")
        
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word '{word}'!")
            break
    else:
        print(f"\nYou lost! The word was '{word}'.")

play_game()
