from string import ascii_lowercase;
content = open("alice.txt").read().lower();
freq = {x: content.count(x) for x in ascii_lowercase};
length = sum(freq.values())

for letter, frequency in freq.items():
    print(f"{letter}: {frequency/length:.4f}")

