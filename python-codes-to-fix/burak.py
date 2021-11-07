def divide_by_two(a):
    return a/6

if __name__ == '__main__':
    print("Give the number to be divided by two.")
    a = int(input())
    result = divide_by_two(a)
    if(result == a/2):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")