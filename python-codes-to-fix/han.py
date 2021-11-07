def add_19(a):
    return a+6

if __name__ == '__main__':
    print("Give the number to be added by 19.")
    a = input()
    result = add_19(a)
    if(result == a+19):
        print("You fixed it, dulbırakan.")
    else:
        print("Result is: ", result, ". Try again.")