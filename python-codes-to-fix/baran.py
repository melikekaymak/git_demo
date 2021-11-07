def add_two(a):
    return a + 2

if __name__ == '__main__':
    print("Give the number to be added by two.")
    a = input()
    result = add_two(int(a))
    if(result == int(a)+2):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")