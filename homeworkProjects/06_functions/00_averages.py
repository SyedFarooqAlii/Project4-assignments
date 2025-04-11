def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a+b
    return sum/2

def main():
    average1 = average(0,10)
    average2 = average(0,8)
    
    final = average(average1,average2)

    print("average1",average1)
    print("average2",average2)
    print(final)

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()