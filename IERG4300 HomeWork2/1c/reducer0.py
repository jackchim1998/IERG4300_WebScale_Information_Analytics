#!/usr/bin/env python

from operator import itemgetter
import sys


current_tri = None
tri = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    tri, nothing = line.split('\t', 1)
    
    if current_tri == tri:
        continue
    else:
        if current_tri:
	    print '%s' % (current_tri)
	current_tri = tri

# do not forget to output the last word if needed!
if current_tri:
    #store in count
    print '%s' % (current_tri)

	
