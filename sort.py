#!/usr/bin/env python
# !source env/bin/activate

import sys

lines = []
for line in sys.stdin:
    lines.append(line)

ans = "\n".join(sorted(lines))
sys.stdout.write(ans)
