import random

DONE_LIKELIHOOD =0.3# 30% chance to stop early

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=" ")
        
def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")     
    chaotic_counting()
    
    print("Im done")


if __name__ == '__main__':
    main()
