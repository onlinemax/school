from string import ascii_uppercase, ascii_lowercase

def build_translation_table(s):
    '''Create a dictionary that will act as a translation table for
    the Caesar cipher using a shift of 's'.'''
    
    lwr = ascii_lowercase
    upr = ascii_uppercase

    letters = lwr + upr
    shifted = lwr[s:] + lwr[:s] + upr[s:] + upr[:s]

    table = {}
    for i in range(len(letters)):
        source = letters[i]
        target = shifted[i]
        table[source] = target
    return table

# Suppose you want to shift by 2 places:
# n = 2 # (a -> c, b -> d, c -> e, d -> f, ... y -> a, z -> b)
# d = build_translation_table(n)
# You can translate a single characters as follows:
# shifted_a = d['a']
# shifted_z = d['z']
# print(shifted_a, shifted_z) # prints c b

# WRITE YOUR PROGRAM HERE...
content = open(input("Enter the the file name to encrypt or decrypt: ")).read()
shift = int(input("Enter the shift amount: "))
table = build_translation_table(shift)

print("".join(list(map(lambda x: table[x] if x.isalpha() else x, content))))

# There was no message.txt included with this lab.
