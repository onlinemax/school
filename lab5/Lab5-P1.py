def get_integer(prompt): 
    tmp = input(prompt)
    if not tmp.isnumeric():
        print("This number isn't an integer!!!")
        return None
    return int(tmp)
def __main__():
    a = get_integer("Enter an int a: ")
    if (a == None):
        return 1
    b = get_integer("Enter an int b: ")
    if (b == None):
        return 1
    while (a != b):
        if (a > b):
            a-=b
        else:
            b-=a
    print("GCD is", a)
__main__()
# GCD is 65
# GCD is 307
# GCD is 1039
# GCD is 2027