#!/usr/bin/env python

from operator import itemgetter
import sys

top_list = []
current_pair = None
pair = None
current_count = 0
count = 0
def sortSecond(val):
    return val[1]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    pair, count_str = line.split('\t', 1)
    # convert to int or double
    try:
	count = int(count_str)
    except ValueError:
	continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_pair == pair:
        current_count += count
    else:
        if current_pair:
	    #store in counter
            top_list.append([current_pair,current_count])
	    
	    if len(top_list)>1000:
		top_list.sort(key=sortSecond,reverse=True)
		del top_list[10:]
	current_pair = pair
        current_count = count

# do not forget to output the last word if needed!
if current_pair:
    #store in count
    top_list.append([current_pair,current_count])

top_list.sort(key=sortSecond,reverse=True)
del top_list[10:]

for item in top_list:
    print '%s\t%d' % (item[0],item[1])

	
