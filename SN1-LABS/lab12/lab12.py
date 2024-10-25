def isanagram(word1: str, word2: str):
    return "".join(sorted(list(word1.lower().replace(" ", ""))))  == "".join(sorted(list(word2.lower().replace(" ", ""))))
def find_duplicates(x):
    list = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if (x[i] == x[j]) and (x[i] not in list):
                list.append(x[i])
                break;
    list.sort()
    return list;
def ismagic(sq):
    accum = sum(sq[0])
    length = len(sq)
    for i in range(length):
        colSum = sum([x[i] for x in sq]);
        if (not sum(sq[i]) == accum) or (not colSum == accum):
            return False;
    return True;

