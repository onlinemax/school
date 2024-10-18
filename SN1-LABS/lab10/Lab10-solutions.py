#Lab 10 Solutions
#Exercise 1
def validate_pwd(pwd):
    digits="0123456789"
    if 8<=len(pwd)<=15 and pwd[len(pwd)-2]=="#" and '0'<=pwd[len(pwd)-1]<='9' and 'A'<= pwd[0]<='Z':
        return True
    else:
        return False

#Exercise 2    
def remaining_fraction(days, half_life):
    '''returns the fraction of radiation left'''
    return 1/(2**(days/half_life))

y = remaining_fraction(120, 120)
print(round(y, 2)) #1/4

y = remaining_fraction(240, 120)
print(round(y, 2)) #1/4

y = remaining_fraction(120, 59.49)
print(round(y, 2)) #0.25

y = remaining_fraction(1200, 1925.35)
print(round(y, 2)) #0.65

#Exercise 3
#pi with while loop
def pi_series(n):
    '''returns an estimation of pi to n terms'''
    k=0
    pi=0
    while k < n: #n terms from k=0 to k=29
        pi=pi+ ((2*(-1)**k)*(3**(0.5-k)))/(2*k+1)
        k=k+1
    return pi

#pi with for loop
def pi_series_2(n):
    '''returns an estimation of pi to n terms'''
    pi=0
    for k in range(n): #n terms from k=0 to k=29
        pi = pi + ((2*(-1)**k)*(3**(0.5-k)))/(2*k+1)
    return pi
        
#test cases for pi
from math import pi
print(pi_series(15))
print(pi_series(30))
print(pi_series_2(15))
print(pi_series_2(30))
print("pi from math module is",pi)
      
#Exercise 4
def distance(u, v):
    '''Returns the distance between 2 vectors'''
    total=0
    for i in range(len(u)): #computes the sum of the differences
        total = (u[i]-v[i])**2
    d = total**0.5 #the distance
    return d

a = [4, 3]
b = [1, -1]
print(distance(a, b))

c = [1.5, 2.0, 3.7]
d = [0.5, -2.0, -4.3]
print(distance(c, d))

    
        
                   

    
