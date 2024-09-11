array = [-21, -20, -18, -15, -14, -13, -11, -10, -8, -7, -6, -5, -4, -3, 3, 5, 8, 10, 12, 14, 16, 17, 19, 22, 23]

def binary_search(number): 
    i = 0
    j = len(array) - 1
    f = 0
    while i <= j:
        k = (i + j) // 2
        print("i:", i, "j", j, "k", k)
        if array[k] == number:
            f = 1
            i = j + 1
        elif array[k] < number:
            i = k + 1
        else:
            j = k - 1
    if f == 1:
        print("present")
    else:
        print("not present")

binary_search(-8)

    