#!/usr/bin/env python
# !source env/bin/activate

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-w", "--words", action='store_true')
parser.add_argument("-l", "--lines", action='store_true')
parser.add_argument("-c", "--length",  action='store_true')

args = parser.parse_args()

def w(file):

    file = sys.stdin


    words = 0
    for line in file:
        words += len(line.split())
    print(words)

def lines_count(file):

    file = sys.stdin


    lines = 0
    for line in file:
        lines += 1
    print(lines)

def length_count(file):

    file = sys.stdin


    length = 0
    for line in file:
        length += len(list(line))
    print(length)

if args.words:
    file = sys.stdin


    w(file)
elif args.lines:
    file = sys.stdin


    lines_count(file)
elif args.length:
    file = sys.stdin


    length_count(file)
else:
    print("Choose action : -w, -l, -c")
