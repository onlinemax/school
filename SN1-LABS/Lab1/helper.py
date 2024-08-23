l = []
while True: 
    x = input("Enter binary number: ")
    if (x == ".finish"):
        break
    l.append(x)
def getNumber(string: str):
     s = string + " = "
     n = 0
     length = len(string) - 1
     for i in range(length, -1, -1):
         n += int(string[length - i]) * 2**i
         s += string[length - i] + f"*2^{i}" + (" + " if i != 0 else "")
     s += f" = {n}"
     return s
for i in l:
    print(getNumber(i))