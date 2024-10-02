from math import pi
# Exercise 1
def validate_password(pwd):
    length = len(pwd)
    return length >= 8 and length <= 15 and pwd[length - 2] == '#' and pwd[length - 1].isnumeric() and pwd[0].isupper()
        
#Test
print( validate_password ('HelloWorld #1')) #prints True
print( validate_password ('A12345678 #9')) #prints True
print( validate_password ('Hello#1')) #prints False
# Exercise 2
def remaining_fraction(days, half_life):
    return 1 / 2 ** (days / half_life)
# Test

y = remaining_fraction (120 , 59.49)
print(round(y, 2)) # Should print 0.25
y = remaining_fraction (1200 , 1925.35) # Should print 0.65
print(round(y, 2))
# Exercise 3 
def pi_series(n):
    accum = 0
    for i in range(n):
        accum += (2 * (-1) ** i * 3 ** (0.5 - i))/ (2 * i + 1)
    return accum
# Test

print(pi_series(30) == pi) # Should print True

# Exercise 4

def distance(u, v):
    accum = 0
    for i in range(len(u)):
        accum += (u[i] - v[i]) ** 2
    return accum ** (1/2)

# Test

a = [4, 3]
b = [1, -1]
print( distance (a, b)) # Should print 5.0

c = [1.5 , 2.0, 3.7]
d = [0.5 , -2.0, -4.3]
print( distance (c, d)) # Should print 9.0

def federal_tax(income):
    table = [[0.15, 53359], [0.205, 106717], [0.26, 165430], [0.29, 235675], [0.33, -1]]
    tax = 0
    last_threshold = 0
    for rate in table: 
        if (rate[1] == -1 or rate[1] >= income):
            tax += rate[0] * (income - last_threshold)
            break
        
        tax += rate[0] * (rate[1] - last_threshold)
        last_threshold = rate[1]
    return tax
    
print( federal_tax (200000)) #should print 44232.92
