import random

NUM_ROUNDS = 5
MIN_VALUE = 1
MAX_VALUE = 100

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0 

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        player_num = random.randint(MIN_VALUE, MAX_VALUE)
        computer_num = random.randint(MIN_VALUE, MAX_VALUE)
        
        print(f"Your number is {player_num}")
        
        guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
        while guess not in ["higher", "lower"]:
            guess = input("Please enter either 'higher' or 'lower': ").strip().lower()
        
        correct = False
        if guess == "higher" and player_num > computer_num:
            correct = True
        elif guess == "lower" and player_num < computer_num:
            correct = True

        if correct:
            print(f"You were right! The computer's number was {computer_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_num}")

        print(f"Your score is now {score}")
        print()  

    print("Thanks for playing!")
    print()

    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
