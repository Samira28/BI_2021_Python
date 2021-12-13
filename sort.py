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
    for line in sys.stdin:
        lines.append(line)

    ans = "\n".join(sorted(lines))
    sys.stdout.write(ans)
else:
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line)
        ans = "\n".join(sorted(lines))
        sys.stdout.write(ans)
