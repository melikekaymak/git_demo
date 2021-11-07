def add_45(a):
    return a + 7

if __name__ == '__main__':
    print("Give the number to be added by 45.")
    a = input()
    result = add_45(a)
    if(result == a+45):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")