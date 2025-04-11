import random

def main():
    n = random.randint(1, 99)
    print("Guess the number between 1 and 99")
    
    while True:
        guess = input("Guess: ")
        
        if not guess.isdigit():
            print("Enter a valid number")
            continue

        g = int(guess)
        
        if g == n:
            print("Correct! Number was:", n)
            break
        elif g < n:
            print("Too low")
        else:
            print("Too high")

if __name__ == '__main__':
    main()
