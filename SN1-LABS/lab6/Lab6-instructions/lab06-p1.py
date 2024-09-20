from math import cos, sin, acos, radians
R = 6371
t1 = radians(float(input("Enter latitude 1: ")))
n1 = radians(float(input("Enter longitude 1: ")))
t2 = radians(float(input("Enter latitude 2: ")))
n2 = radians(float(input("Enter longitude 2: ")))
# add your import statement and appropriate calculations here.
def greatCircleDistance(t1, n1, t2, n2): 
    R = 6371
    return R * acos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(n1 - n2))
print(greatCircleDistance(t1, n1, t2, n2))