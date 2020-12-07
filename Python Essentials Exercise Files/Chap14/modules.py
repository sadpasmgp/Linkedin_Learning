#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys
import os
import random
import datetime

def main():
    v = sys.version_info
    z = sys.platform
    print('Python version {}.{}.{}'.format(*v))
    print(z)
    print(os.name)
    print(os.getenv('PATH'))
    print(os.getcwd())
    print(os.urandom(25))
    print(os.urandom(25).hex())
    print(random.randint(1, 1000))
    print(datetime.datetime.now())
    

if __name__ == '__main__': main()
