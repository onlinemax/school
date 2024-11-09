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
filename = input("Enter a filename: ");
shift = int(input("Enter the shift amount (0-25):"));
table = build_translation_table(shift);
content = open(filename).read();
encrypted = "".join([table[x] if x.isalpha() else x for x in content]);
print(encrypted);

# This is the text: 
"""
 The Zen of Python
 
 Beautiful is better than ugly.
 Explicit is better than implicit.
 Simple is better than complex.
 Complex is better than complicated.
 Flat is better than nested.
 Sparse is better than dense.
 Readability counts.
 Special cases aren't special enough to break the rules.
 Although practicality beats purity.
 Errors should never pass silently.
 Unless explicitly silenced.
 In the face of ambiguity, refuse the temptation to guess.
 There should be one-- and preferably only one --obvious way to do it.
 Although that way may not be obvious at first unless you're Dutch.
 Now is better than never.
 Although never is often better than right now.
 If the implementation is hard to explain, it's a bad idea.
 If the implementation is easy to explain, it may be a good idea.
"""
