def mod_by_two(a):
    return a%2

if __name__ == '__main__':
    print("Give the number to be taken its mode by two.")
    a = input()
    result = mod_by_two(a)
    if(result == a%2):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")