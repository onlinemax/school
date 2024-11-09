from string import ascii_lowercase

def build_table(s: int):
    table = {}
    for i in range(26):
        table[ascii_lowercase[i]] = ascii_lowercase[(i - s + 26) % 26]
        table[ascii_lowercase[i].upper()] = ascii_lowercase[(i - s + 26) % 26].upper()
    return table
content = open('sample.txt').read()
print([[d, content.count(d)] for d in ascii_lowercase])
most_frequent = sorted([[d, content.count(d)] for d in ascii_lowercase], reverse=True, key=lambda x: x[1])[0]
print(most_frequent)
