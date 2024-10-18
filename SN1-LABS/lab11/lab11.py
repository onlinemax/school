def sumsq(x):
    accum = 0
    for i in x:
        accum += i * i
    return accum
def average(x):
    accum = 0
    if (len(x) == 0):
        return accum
    for i in x:
        accum += i
    return accum / len(x)   
# Exercise 3
def is_pangram(x):
    if (len(x) < 26):
        return False
    set = [1] * 26;
    different = 0
    for i in x:
        index = ord(i) - ord('a')
        if index < 0 or index > 26:
            index = ord(i) - ord('A')
        if index >= 0 and index <= 26 and set[index] == 1:
            set[index] = 0
            different += 1
    return different >= 26 

