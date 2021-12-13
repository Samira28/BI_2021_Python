#!/usr/bin/env python
# !source env/bin/activate

import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--all", action='store_true')

args = parser.parse_args()

if args.all:
    sys.stdout("\n".join(os.listdir()))
else:
    sys.stdoutl("Oops")
