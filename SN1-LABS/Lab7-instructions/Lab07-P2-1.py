dna = input("Enter a DNA sequence: ")
complement = ""
for i in range(0, len(dna)):
    c = dna[i]
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
    
