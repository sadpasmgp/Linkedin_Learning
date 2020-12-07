#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

print('Hello, World.')

x = ( 1, 2, 3, 4, 5 )
y = list(reversed(x))
print(x)
print(y)

y = sum(x)
print(y)

print(max(x))
print(min(x))

print(all(x))

y = (6, 7, 8, 9)
z = zip(x, y)
for a, b in z:
    print(a, b)

x = ('cat', 'rabbit', 'dog')
for i, v, in enumerate(x):
    print(i, v)

x = 43
y = isinstance(x, int)
print(x)
print(y)
print(id(x))
