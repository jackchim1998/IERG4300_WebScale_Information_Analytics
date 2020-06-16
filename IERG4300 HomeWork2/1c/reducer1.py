#!/usr/bin/env python

from operator import itemgetter
import sys
arr = []
current_tri = None
current_count = 0
tri = None
count = None
max_print=2000
no_of_baskets=0
threshold=0.0025
def sortsecond(val):
    return val[1]
with open('count_file','r') as fp:
    content = fp.read()
    count,smth = content.split(' ', 1)
    try:
        no_of_baskets = int(count)
    except ValueError:
        print "value error"
        no_of_baskets = 0

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    tri, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
	
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_tri == tri:
        current_count += count
    else:
        if current_tri:
            # write result to STDOUT	    
	    arr.append([current_tri,current_count])
            if len(arr) >(max_print*20):
		arr.sort(key=sortsecond,reverse=True)
		del arr[max_print:]
        current_count = count
        current_tri = tri

# do not forget to output the last word if needed!
if current_tri == tri:
    arr.append([current_tri,current_count])
pass_count = threshold * no_of_baskets
arr.sort(key=sortsecond,reverse=True)
if len(arr) >=max_print:
    del arr[max_print:]
for i in range(len(arr)):
    if arr[i][1] >= pass_count:
	print '%s\t%d' % (arr[i][0],arr[i][1])
