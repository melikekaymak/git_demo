def add_2016(a):
    return a+2000

if __name__ == '__main__':
    print("Give the number to be added by 2016.")
    a = input()
    result = add_2016(a)
    if(result == a+2016):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")