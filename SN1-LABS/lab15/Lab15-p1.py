# Python 3.12.7 (main, Oct  1 2024, 11:15:50) [GCC 14.2.1 20240910] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> x = 1000
# >>> y = 21
# >>> z = "Marianopolis"
# >>> ls = [30, 2, -14]
# >>> for v in ls:print(x / y)
# ... print(v)
#   File "<stdin>", line 2
#     print(v)
#     ^^^^^
# SyntaxError: invalid syntax
# >>> for v in ls:print(x / y)
# ...     print(v)
#   File "<stdin>", line 2
#     print(v)
# IndentationError: unexpected indent
# >>> for v in ls:print(x / y)
# ... print(x / y)
#   File "<stdin>", line 2
#     print(x / y)
#     ^^^^^
# SyntaxError: invalid syntax
# >>> for v in ls:
# ...     print(v)
# ... 
# 30
# 2
# -14
# >>> print(f'{x / y:8.3f}')
#   47.619
# >>> for v in ls:
# ...     print(f'{v:4d}')
# ... 
#   30
#    2
#  -14
# >>> text = f"There were only {y} chairs for {ls[0]} students."
# >>> print(text)
# There were only 21 chairs for 30 students.
# >>> print(f'{ls[1]} minus {ls[2]} equals {ls[1] - ls[2]}')
# 2 minus -14 equals 16
# >>> print(f'{z} College was founded in {x+908}')
# Marianopolis College was founded in 1908
# >>> n = 0.01
# >>> while n < 10000:
# ... print(f'{n:8.2f}')
#   File "<stdin>", line 2
#     print(f'{n:8.2f}')
#     ^
# IndentationError: expected an indented block after 'while' statement on line 1
# >>> n *= 10
# >>> n = 0.01
# >>> while n < 10000:
# ... print(f'{n:8.2f}')
#   File "<stdin>", line 2
#     print(f'{n:8.2f}')
#     ^
# IndentationError: expected an indented block after 'while' statement on line 1
# >>> n = 0.001
# >>> n - 0.01
# -0.009000000000000001
# >>> n = 0.01
# >>> while n < 10000:
# ...     printf(f"{n'8.2f}")
#   File "<stdin>", line 2
#     printf(f"{n'8.2f}")
#                ^
# SyntaxError: unterminated string literal (detected at line 2)
# >>>     printf(f"{n:8.2f}")
#   File "<stdin>", line 1
#     printf(f"{n:8.2f}")
# IndentationError: unexpected indent
# >>> while n < 10000:
# ...     printf(f"{n:8.2f}")
# ...     n *= 10
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# NameError: name 'printf' is not defined. Did you mean: 'print'?
# >>>     print(f"{n:8.2f}")
#   File "<stdin>", line 1
#     print(f"{n:8.2f}")
# IndentationError: unexpected indent
# >>> while n < 10000:
# ...     print(f"{n:8.2f}")
# ...     n *= 10
# ... 
#     0.01
#     0.10
#     1.00
#    10.00
#   100.00
#  1000.00
# >>> n = 1
# >>> while n <= 100000:
# ...     print(f'{n:4d}')
# ...     n *= 10
# ... 
#    1
#   10
#  100
# 1000
# 10000
# 100000
# >>> 
