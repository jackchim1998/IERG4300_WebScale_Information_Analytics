#!/usr/bin/env python

from operator import itemgetter
import sys


current_pair = None
pair = None
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    pair, nothing = line.split('\t', 1)
    
    if current_pair == pair:
        continue
    else:
        if current_pair:
	    print '%s' % (current_pair)
	current_pair = pair

# do not forget to output the last word if needed!
if current_pair:
    #store in count
    print '%s' % (current_pair)

	
