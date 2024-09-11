n = 325
a = 0
b = 1
while n > 0:
    t = a + b
    a = b
    b = t 
    n = n - 1
print(a)

# For input 12 output  = 144
# for input 23 output = 28657
# for input 99 ouput= 218922995834555169026
# for input 325 ouput = 37281903592600898879479448409585328515842582885579275203077366912825