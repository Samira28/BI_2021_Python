#!/usr/bin/env python
# !source env/bin/activate

import sys
import argparse

parser = argparse.ArgumentParser()

#Optional
parser.add_argument('--n', type=int, required=True)
parser.add_argument('infile', metavar = 'FILE', nargs = "?", help = 'input file', default='-')

args = parser.parse_args()


file = args.infile
if file == "-":
    
    lines = []

    for line in sys.stdin:
        lines.append(line)
    for i in reversed(range(len(lines)-1, len(lines)-args.n -1, -1)):
        print("".join(lines[i]))
else:
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line)
        for i in reversed(range(len(lines)-1, len(lines)-args.n -1, -1)):
            print("".join(lines[i]))
