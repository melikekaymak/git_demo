def add_six(a):
    return a+2

if __name__ == '__main__':
    print("Give the number to be added by four.")
    a = input()
    result = add_six(a)
    if(result == a+6):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")