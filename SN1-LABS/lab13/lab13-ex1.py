# Python 3.12.7 (main, Oct  1 2024, 11:15:50) [GCC 14.2.1 20240910] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> olours = {'red ':10, 'blue ':20, 'green ':30 }
# >>> print(len( colours ), colours )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'colours' is not defined. Did you mean: 'olours'?
# >>> oolours = {'red ':10, 'blue ':20, 'green ':30 }
# >>> print(len( colours ), colours )
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'colours' is not defined. Did you mean: 'olours'?
# >>> colours = {'red ':10, 'blue ':20, 'green ':30 }
# >>> print(len( colours ), colours )
# 3 {'red ': 10, 'blue ': 20, 'green ': 30}
# >>>  colours ['yellow '] = 40
#   File "<stdin>", line 1
#     colours ['yellow '] = 40
# IndentationError: unexpected indent
# >>> colours ['orange '] = 50
# >>> colours ['yellow '] = 40
# >>> print(len( colours ), colours )
# 5 {'red ': 10, 'blue ': 20, 'green ': 30, 'orange ': 50, 'yellow ': 40}
# >>> for x in colours :
# ... print(x, colours [x])
#   File "<stdin>", line 2
#     print(x, colours [x])
#     ^
# IndentationError: expected an indented block after 'for' statement on line 1
# >>> for x in colours :
# ...     print(x, colours [x])
# ... 
# red  10
# blue  20
# green  30
# orange  50
# yellow  40
# >>> for item in colours .items ():
# ...     print(item)
# ... 
# ('red ', 10)
# ('blue ', 20)
# ('green ', 30)
# ('orange ', 50)
# ('yellow ', 40)
# >>> print(max( colours .values ()), max( colours .keys ()), max( colours ))
# 50 yellow  yellow 
# >>> print(sum(coulours.values()))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'coulours' is not defined. Did you mean: 'colours'?
# >>> print(sum(colours.values()))
# 150
# >>> for x in co
# colours      compile(     complex(     continue     copyright()  
# >>> for x in colours:
# ...     coulours[x] += 1
# ... 
# Traceback (most recent call last):
#   File "<stdin>", line 2, in <module>
# NameError: name 'coulours' is not defined. Did you mean: 'colours'?
# >>> for x in colours:
# ...     colours[x] += 1
# ... 
# >>> print(coulours)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'coulours' is not defined. Did you mean: 'colours'?
# >>> print(colours)
# {'red ': 11, 'blue ': 21, 'green ': 31, 'orange ': 51, 'yellow ': 41}
# >>> print( colours ['pink '])
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'pink '
# >>> print( colours .get('red ', 103) , colours .get('pink ', 103))
# 11 103
# >>> x = {'a': 10, 'c': 11, 'z': 12 }
# >>> y = {'z': 12, 'a': 10, 'c': 11 }
# >>> print(x == y)
# True
# >>> y['z'] -= 1
# >>> print(x == y)
# False
# >>> from string import ascii_lowercase
# >>> letters = dict. fromkeys ( ascii_lowercase , 0)
# >>> print( letters )
# {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
# >>> colours = ('red ', 'green ', 'blue ', 'black ', 'magenta ')
# >>> cdict = dict. fromkeys (colours , 0.0)
# >>> print(cdict)
# {'red ': 0.0, 'green ': 0.0, 'blue ': 0.0, 'black ': 0.0, 'magenta ': 0.0}
