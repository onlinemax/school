# P1

dna = "ATGAATTCTC"
dna_len= len(dna)
print(dna[0])
print(dna[dna_len- 1])
print(dna[0:3])
print(dna[-3:])
new_dna = dna + "!"
print(new_dna)
#It results in an error since we are accesing dna outside of its length
# 1.2
x = [5, -1, 2, 0, 2, 8]
y = [3, 4, 5]
print(len(x))
x[0] = x[0] + 1
print(x)
x = x  + [1]
print(x)
w = x + y
print(w)