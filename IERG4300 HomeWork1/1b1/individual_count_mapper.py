#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line
    words = line.split(",")
    # output
    print '%s\t%s' % (words[0], 1)
