#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s)
print(s.upper())
print(s.lower())
print(s.title())
print(s.swapcase())
print(s.split())
print(s.split('i'))

print(s.count('s'))
print(s[::-1])
print(s.capitalize())
print(s.casefold())

x = 34 * 82 * 75 * 1000
print('the number is {:,}'.format(x))
print('the number is {:,}'.format(x).replace(',', '.'))
print('the number is {:,f}'.format(x))
print('the number is {:.3f}'.format(x))
print('the number is {:b}'.format(x))
print(f'the number is {x}')
print(f'the number is {x:.3f}')