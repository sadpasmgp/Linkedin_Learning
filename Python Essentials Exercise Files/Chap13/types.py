#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x)

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

y = float(x)
print(f'y is {type(y)}')
print(f'y is {y}')

y = complex(x)
print(f'y is {type(y)}')
print(f'y is {y}')

y = str(x)
print(f'y is {type(y)}')
print(f'y is {y}')

y = bool(x)
print(f'y is {type(y)}')
print(f'y is {y}')

x = 47
y = divmod(x, 3)
print(y)

s = 'Hello world'
print(s)
print(repr(s))

class bunny:
    def __init__(self, n):
        self._n = n
    def __repr__(self):
        return f"repr: the number of bunnies is {self._n}🖖"
    
    def __str__(self):
        return f"str: the number of bunnies is {self._n}🖖"

x = bunny(47)
print(ascii(x))
print(chr(128406))
print(ord('🖖'))