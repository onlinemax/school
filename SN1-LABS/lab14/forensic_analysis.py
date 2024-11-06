import pathlib as pl
from typing import List 
p = pl.Path("mystery_folder")

def examinateCase(path: pl.Path) -> list[tuple[str, int]]:
    queue: List[tuple[str, pl.Path]] = []
    queue.append((path.name, path))
    x: List[tuple[str, int]] = []
    while len(queue) != 0:
        prefix, p = queue.pop()
        for child in p.iterdir():
            path_name = prefix + "/" + child.name
            if child.is_dir():
                queue.append((path_name, child))
                continue
            if child.suffix != ".txt": continue
            x.append((path_name, child.read_text().count("formula")))
    return x
cases = examinateCase(p)
sum = 0
max = cases[0]
for name, occurences in cases:
    sum += occurences
    if max[1] < occurences:
        max = (name, occurences)
print("All occurences of formula accross all files in mystery_folder:", sum)
print("The file with the greates occurrence is", max[0], "with", max[1], "occurences");
print("Text inside of", max[0], ":\n", open(max[0]).read())

