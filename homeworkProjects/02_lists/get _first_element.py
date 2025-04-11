def get_first_element(lst):
    print("The first element of the list is :" , lst[0])  # Print the first element of the list

def main():
    # lst = []  # Initialize an empty list
    # n = int(input("How many elements in the list? "))  # Prompt user for number of elements
    # for i in range(n):
    #     element = input("Enter an element: ")  # Get each element from the user
    #     lst.append(element)  # Add the element to the list
    # get_first_element("The first element of the list is ",lst)  # Call the function to print the first element
    # i+=n
    lst =[]
    n = int(input("How many elements in the list :"))
    for i in range(n):
        element =input("Enter an element : ")
        lst.append(element)
    get_first_element( lst)
    
    i+=n
if __name__ == '__main__':
    main()
