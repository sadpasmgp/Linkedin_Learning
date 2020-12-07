#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    try:
        x = int('foo')
        x = 5/0
    except ValueError:
        print("I caught a value error")
    except ZeroDivisionError:
        print('Dont divide by zero')
    except:
        print(f"unknown error: {sys.exc_info()[1]}")
        
    else:
        print('good job!')
        print(x)

if __name__ == '__main__': main()
