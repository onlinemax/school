from os import close
import matplotlib.pyplot as plt
from string import ascii_lowercase
fig, ax = plt.subplots()
content = open("alice.txt").read().lower()

letter = {x: content.count(x) for x in ascii_lowercase}
x = []
y = []
for i in sorted(list(letter.items()), key=lambda x: x[1]):
    x.append(i[0])
    y.append(i[1])
print(x, y)
ax.bar(x, y);
ax.set_title("Frequency of the letters through Alice.txt")
plt.show()
