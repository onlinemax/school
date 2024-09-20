import turtle as tu
from sys import exit
from time import sleep 
import math
a = int(input("Enter first length: "))
b = int(input("Enter second length: "))
c = int(input("Enter third length: "))
try:
    d = math.acos((-(c * c) + a * a + b * b) / (2 * a * b))
except:
    print("Imposible")
    exit(1)
first = (0 , 0)
second = (a, 0)
third = (a -  b * math.cos(d), b * math.sin(d))
tu.color("black", "red")
tu.speed(1)
tu.width(5)
tu.delay(50)
tu.begin_fill()
tu.pendown()
tu.goto(first)
tu.goto(second)
tu.goto(third)
tu.goto(first)
tu.end_fill()

tu.mainloop()
