#!/usr/bin/env python
# !source env/bin/activate

import sys
import argparse

parser = argparse.ArgumentParser()

#Optional
parser.add_argument("-w", "--words", action='store_true')
parser.add_argument("-l", "--lines", action='store_true')
parser.add_argument("-c", "--length",  action='store_true')

parser.add_argument('infile', metavar = 'FILE', nargs = "?", help = 'input file', default='-')


args = parser.parse_args()


def w(file):
    file = args.infile
    if file == "-":
        file = sys.stdin
        words = 0
        for line in file:
            words += len(line.split())
        print(words)
    else:
        words = 0
        with open(file, "r") as f:
            for line in f:
                words += len(line.split())
            print(words)
    
                
def lines_count(file):
    file = sys.stdin
    lines = 0
    for line in sys.stdin:
            lines += 1
    print(lines)
    
def length_count(file):
    file = sys.stdin
    length = 0
    for line in sys.stdin:
            length += len(list(line))
    print(length)
    

if args.words:
    file = args.infile
    w(file)
elif args.lines:
    file = args.infile
    lines_count(file)
elif args.length:
    file = args.infile
    length_count(file)
else:
    print("Choose action : -w, -l, -c")
