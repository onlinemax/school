from string import ascii_lowercase
content = open("alice.txt").read().lower()
frequencies = {}
size = 0
for i in ascii_lowercase:
    frequencies[i] = content.count(i);
    size += frequencies[i]
for item, value in frequencies.items():
    print(f"{item}: {value / size:.4f}")
