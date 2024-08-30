def getNumber(string: str):
     s = string + " = "
     n = 0
     length = len(string) - 1
     for i in range(length, -1, -1):
         n += int(string[length - i]) * 2**i
         s += string[length - i] + f"*2^{i}" + (" + " if i != 0 else "")
     s += f" = {n}"
     return s
def invertNumber(string: str):
    s = ""
    for char in string:
        s += "0" if (char == "1") else "1"
    return s
def addOne(string: str):
    return bin(int(string, base=2) + 1)[2:]
def isBinary(s) -> bool:
    for c in s:
       if (c != "1" and c != "0"):
           return False
    return True
def getFunction(s):
    match s:
        case "number":
            return getNumber
        case "invert":
            return invertNumber
        case "one":
            return addOne
        case _:
            return "none"

l = []
while True:
    x = input("Enter an input: ")
    if x == ".exit":
        break
    if getFunction(x) != "none":
        l.append(getFunction(x))
        print("done")
    if (isBinary(x)):
        l.append(x)
        print("done")
f = getNumber
print("The results: ")
for x in l:
    if callable(x):
        f = x
    else:
        print(f(x))

