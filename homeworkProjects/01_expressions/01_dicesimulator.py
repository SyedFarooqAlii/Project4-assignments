import random
num_dice =6 
def roll_dice():
    die1 = random.randint(1, num_dice)
    die2 = random.randint(1, num_dice)
    total = die1 +  die2
    print("The total of dice is ", total)
    
def main():
    die_1:int = 10 
    print("The Die one in main starts as " + str(die_1))   
    roll_dice()
    roll_dice()
    roll_dice()
    print("The Die_1 in main is " + str(die_1))
    
if __name__ == '__main__':
    main()