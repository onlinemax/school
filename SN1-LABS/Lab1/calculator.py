def getNumber(s: str, index: int = 0):
    i = index
    commaFound = False
    while (i < len(s)):
        if (x[i] == "."):
            if commaFound:
                raise Exception("There should not be two comma in a number")
            commaFound = True
        elif(not (x[i].isnumeric() or (x[i] == "-" and i == 0))):
            break
        i+=1
    return [i, float(s[index:i])]


x = input()
print(f"The number is {getNumber(x)[1]}")