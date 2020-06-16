#!/usr/bin/env python

import sys
similar=0.0
cuid_last2_digit=82
pair=''
similar_str=''
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    pair, similar_str = line.split('\t',1)
    
    userid = pair.split(',')
    try:
	similar = float(similar_str)
	userid[0] = int(userid[0])
	userid[1] = int(userid[1])
    except ValueError:
	continue
    # filter out similar 0
    if userid[0]%100 == cuid_last2_digit:
	print '%d\t%d %f' % (userid[0],userid[1],similar)
    if userid[1]%100 == cuid_last2_digit:
        print '%d\t%d %f' % (userid[1],userid[0],similar)    
