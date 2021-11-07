def add_thirty_one(a):
    return a+6

if __name__ == '__main__':
    print("Give the number to be added by 31.")
    a = input()
    result = add_thirty_one(a)
    if(result == a+31):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". meh. Try again.")