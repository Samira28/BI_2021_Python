#!/usr/bin/env python
# !source env/bin/activate

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--d', type=str, required=True)
parser.add_argument("-r","--remove", action='store_true')

args = parser.parse_args()

if args.remove:
    for root, dirs, files in os.walk(args.d, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
        os.rmdir(root)
