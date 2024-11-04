def grade_distribution(L: list[int]):
  return {x: L.count(x) for x in L}
def column(col: int, x: list[list[int]]):
  l = []
  for a in x:
    l.append(a[col])
  return l
def ismagic(x: list[list[int]]):
  right = sum(x[0]);
  length = len(x)
  for i in range(length):
    col = column(i, x);
    # print(len({d: True for d in x[i]}), len({d: True for d in col}), length, sum(col), sum(x[i]), right); #For debug purposes
    if len({d: True for d in x[i]}) != length or len({d: True for d in col}) != length or sum(col) != right or sum(x[i]) != right:
      return False;
  return True

print(ismagic([[5 ,10 , 1, 3],
                [10, 4, 2, 3],
                [1, 2, 8, 5],
                [3, 3, 5, 0]]))
