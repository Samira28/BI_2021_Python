#!/usr/bin/env python
# !source env/bin/activate

import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--n', type=int, required=True)

args = parser.parse_args()

lines = []

for line in sys.stdin:
    lines.append(line)
for i in reversed(range(len(lines)-1, len(lines)-args.n -1, -1)):
    print("".join(lines[i]))
