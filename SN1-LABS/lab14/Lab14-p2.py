from string import ascii_lowercase
#open and read the entire file alice.txt here
text = open("alice.txt");
content = text.read().lower()
text.close()

#create the dictionary frequencies
frequencies=dict.fromkeys(ascii_lowercase,0)

#continue your code here
for i in ascii_lowercase:
    frequencies[i] = content.count(i);
for i in ascii_lowercase:
    print(f"letter {i}: {frequencies[i]} characters")
