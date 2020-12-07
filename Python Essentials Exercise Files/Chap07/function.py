#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(5)

def kitten(n):
    print(f'{n} : Meow.')

def animal(legs=4, sound='barks', animal='dog', tail='short'):
    print(f'{animal} {sound}. it has {legs} legs and {tail} tail')

#def animals_all(fname, legs, sound, tail):
#   print(f'{fname} has {legs} legs. It makes {sound} sound. It has {tail} tail')

def animals_all(*args):
    args = ('parrot', '2','human-like' , 'green')
    print(f'{args[0]} has {args[1]} legs. It makes {args[2]} sound. It has {args[3]} tail')

if __name__ == '__main__': 
    animal()
    animal(4, 'roars','tiger','long')
    animals_all( )
