#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open(r'C:\Users\sp\Downloads\Master Python for Datascience\03Python Essential Training\Ex_Files_Python_EssT\Exercise Files\Chap12\lines.txt')
    for line in f:
        print(line.rstrip())

if __name__ == '__main__': main()
