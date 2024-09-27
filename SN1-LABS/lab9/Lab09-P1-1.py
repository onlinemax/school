dna = input("Enter a DNA sequence: ")
complement = ""
for c in dna:
    if c == 'A':
        c = 'T'
    elif c == 'T':
        c = 'A'
    elif c == 'C':
        c = 'G'
    elif c == 'G':
        c = 'C'
    complement += c
print("The complement is", complement)
    
