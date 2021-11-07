def multiply_by_two(a):
    return a*2

if __name__ == '__main__':
    print("Give the number to be multiplied by two.")
    a = input()
    result = multiply_by_two(a)
    if(result == a*2):
        print("You fixed it.")
    else:
        print("Result is: ", result, ". Try again.")