#!/usr/bin/env python
#!source env/bin/activate

import sys
import argparse



lines = []
for line in sys.stdin:
    lines.append(line)
list_of_unique_lines = []
unique_lines = set(lines)

for line in unique_lines:
    list_of_unique_lines.append(line)
for i in reversed(range(len(list_of_unique_lines)-1)):
    sys.stdout.write("".join(list_of_unique_lines[i]))
