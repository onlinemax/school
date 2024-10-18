from Lab10_solutions import remaining_fraction

assert remaining_fraction(120, 120) == 0.5
assert remaining_fraction(240, 120) == 0.25
assert round(remaining_fraction(120, 59.49),2) == 0.25
assert round(remaining_fraction(1200, 1925.35),2) == 0.65 

print("The remaining_fraction function is correct.")


from Lab10_solutions import validate_pwd
assert validate_pwd('HelloWorld#1') == True
assert validate_pwd('A12345678#9') == True
assert validate_pwd('Hello#1')== False
assert validate_pwd('HelloWorld#')== False
assert validate_pwd('helloWorld#1')== False

print("The validate_password function is correct.")

from Lab10_solutions import pi_series
import math

assert pi_series(30) != math.pi


print("The pi_series function is correct.")
