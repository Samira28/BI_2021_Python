#!/usr/bin/env python
#!source env/bin/activate

import os
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--d', type=str, required=True)
parser.add_argument("-p","--parent", action='store_true')
args = parser.parse_args()

if args.parent:
    os.makedirs(args.d)
