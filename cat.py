#!/usr/bin/env python
# !source env/bin/activate

import sys
import argparse

parser.add_argument('infile', metavar = 'FILE', nargs = "?", help = 'input file', default='-')

args = parser.parse_args()

file = args.infile
if file == "-":
    for line in file:
        print(line)
else:
    with open(file, "r") as f:
        for line in f:
            print(line)
