#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open(r'C:\Users\sp\Downloads\Master Python for Datascience\03Python Essential Training\Ex_Files_Python_EssT\Exercise Files\Chap12\lines.txt','r')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        print('.', end='', flush=True)
    outfile.close()
    print('\ndone.')

if __name__ == '__main__': main()
