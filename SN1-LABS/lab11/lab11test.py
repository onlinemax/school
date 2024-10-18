# Verify that the sumsq function is working.


from lab11 import sumsq
assert sumsq([]) == 0
assert sumsq([1]) == 1
assert sumsq([2, 3]) == 13
assert sumsq([3.5, 2.5]) == 18.5
assert sumsq([3, -4, 5]) == 50
assert sumsq([1, 0, -1, 0, 1, 0, -1]) == 4

print("The sumsq function is correct.")

from lab11 import average
assert average(([1 ,2 ,3 ,4])) == 2.5
assert average([]) == 0
assert average([1.5 , -2.0, -3.0, 3.5]) == 0.0

print("The average function is correct.")

from lab11 import is_pangram
assert is_pangram("The quick brown fox jumps over the lazy dog") == True
assert is_pangram("Pack my box with five dozen liquor jugs") == True
assert is_pangram("The quick brown fox jumps over the lazy cat") == False
       
print("All lab 11 tests passed.")

