def add_four(a):
    return a+6

if __name__ == '__main__':
    print("Give the number to be added by four.")
    a = input()
    result = add_four(a)
    if(result == a+4):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")