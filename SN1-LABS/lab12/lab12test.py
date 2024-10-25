from lab12 import isanagram, find_duplicates, ismagic
# Anagrams test

assert isanagram ("Mango", "Among") == True
assert isanagram ("BELOW", "elbow") == True
assert isanagram (" stressed ", " desserts ") == True
assert isanagram ("rod","door") == False
assert isanagram (" Marianopolis ", " Airmail Snoop")
print("Anagram Test Passed");

# Find Duplicates Test

assert find_duplicates([
    734, 281, 212, 297, 312, 733, 703, 426, 220, 277,
    367, 304, 830, 481, 994, 910, 46, 6, 246, 960,
    644, 684, 78, 30, 90, 175, 241, 573, 55, 838,
    976, 996, 884, 798, 375, 477, 293, 687, 910, 379,
    259, 557, 955, 872, 620, 699, 178, 743, 681, 861,
    838, 177, 524, 990, 259, 243, 182, 893, 341, 823,
    979, 464, 287, 567, 106, 977, 590, 281, 722, 68,
    230, 907, 119, 99, 275, 678, 218, 543, 57, 595,
    989, 216, 136, 943, 959, 835, 141, 101, 729, 712,
    670, 104, 836, 614, 301, 786, 567, 668, 89, 918
]) == [259 , 281, 567, 838, 910];

assert find_duplicates([2, 1, 6, 3, 1, 2, 4, 2, 5]) == [1, 2]
print("Duplicates tested passed");

# Magic Test:
assert ismagic([[16 , 3, 2, 13],
                [5, 10, 11, 8],
                [9, 6, 7, 12],
                [4, 15, 14, 1]]) == True;

assert ismagic([[5 ,10 , 1, 3],
                [10, 4, 2, 3],
                [1, 2, 8, 5],
                [3, 3, 5, 0]]) == False;

assert ismagic([[2, 7, 6], [9, 5, 1], [4, 3, 8]]) == True;

assert ismagic([[2, 16, 13, 3], [11, 5, 8, 10], [7, 9, 12, 6], [14, 4, 1, 15]]) == True;

assert ismagic([[11 , 24, 7, 20, 3], [4, 12, 25, 8, 16], [17, 5, 13, 21, 9],
                [10, 18, 1, 14, 22], [23, 6, 19, 2, 15]]) == True;

assert ismagic([[22 ,27 ,20 ,31 ,9 ,2] ,
                [21 ,23 ,25 ,3 ,32 ,7] ,
                [26 ,19 ,24 ,35 ,1 ,6] ,
                [13 ,18 ,11 ,4 ,36 ,29] ,
                [12 ,14 ,16 ,30 ,5 ,34] ,
                [17 ,10 ,15 ,8 ,28 ,33]]) == True;

assert ismagic([[2 , 6, 7], [9, 5, 1], [4, 3, 8]]) == False;

assert ismagic([[2 , 16, 13, 3], [11, 5, 8, 10], [7, 9, 12, 6], [15, 4, 14, 1]]) == False;

print("Magic Test Passed");
