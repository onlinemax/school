from string import ascii_lowercase,  ascii_letters
content = open("message.txt").read()
freq = {x: content.count(x) for x in ascii_letters}
most_frequent = list(sorted(freq.items(), key=lambda x: x[1], reverse=True)[:2])
def build_shifted_table(s):
    dic = {}
    for i in range(len(ascii_lowercase)):
        dic[ascii_lowercase[i]] = ascii_lowercase[(26 + i - s) % 26];
        dic[ascii_lowercase[i].upper()] = ascii_lowercase[(26 + i - s) % 26].upper();
    return dic

#I guess that the most frequent letter in the english alphabet is e index()
shift_amount = ascii_lowercase.index(most_frequent[0][0]) - ascii_lowercase.index('e');
table = build_shifted_table(shift_amount)
decrypted = "".join([table[x] if x.isalpha() else x for x in content])
print(decrypted)
