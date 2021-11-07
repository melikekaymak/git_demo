def add_two(a):
    return a + 7

if __name__ == '__main__':
    print("Give the number to be added by two.")
    a = input()
    result = add_two(a)
    if(result == a+2):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")