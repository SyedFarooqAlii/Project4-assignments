def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except IndexError:
        return "Invalid indices."

def index_game():
    lst = [1, 2, 3, 4, 5]
    print("Welcome to the Index Game!")
    print("You can 'access', 'modify', 'slice', or type 'quit' to exit.")

    while True:
        print("\nCurrent list:", lst)
        operation = input("Enter operation: ").strip().lower()

        if operation == "quit":
            print("Thanks for playing!")
            break
        elif operation == "access":
            try:
                index = int(input("Enter index to access: "))
                print("Value at index", index, "is:", access_element(lst, index))
            except ValueError:
                print("Please enter a valid integer index.")
        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print("Updated list:", modify_element(lst, index, new_value))
            except ValueError:
                print("Invalid index.")
        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print("Sliced list:", slice_list(lst, start, end))
            except ValueError:
                print("Please enter valid numbers.")
        else:
            print("Invalid operation. Please try again.")

index_game()
