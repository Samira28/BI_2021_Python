#!/usr/bin/env python
# !source env/bin/activate

import sys
import argparse

parser.add_argument('infile', metavar = 'FILE', nargs = "?", help = 'input file', default='-')

args = parser.parse_args()

file = args.infile
if file == "-":
    file = sys.stdin
    lines = []
    for line in file:
        lines.append(line)
    list_of_unique_lines = []
    unique_lines = set(lines)

    for line in unique_lines:
        list_of_unique_lines.append(line)
    for i in reversed(range(len(list_of_unique_lines)-1)):
        sys.stdout.write("".join(list_of_unique_lines[i]))
else:
    with open(file, "r") as f:
        for line in f:
            lines.append(line)
        list_of_unique_lines = []
        unique_lines = set(lines)

        for line in unique_lines:
            list_of_unique_lines.append(line)
        for i in reversed(range(len(list_of_unique_lines)-1)):
            sys.stdout.write("".join(list_of_unique_lines[i]))
