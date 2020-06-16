#!/usr/bin/env python

from operator import itemgetter
import sys
arr = []
current_pair = None
current_count = 0
pair = None
count = None
max_print=40
no_of_baskets=0
threshold=0.005
def sortsecond(val):
    return val[1]
#with open('./count.txt','r') as fp:
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
    pair, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
	
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_pair == pair:
        current_count += count
    else:
        if current_pair:
            # write result to STDOUt
	    arr.append([current_pair,current_count])
            if len(arr) >(max_print*20):
		arr.sort(key=sortsecond,reverse=True)
		del arr[max_print:]
        current_count = count
        current_pair = pair

# do not forget to output the last word if needed!
if current_pair == pair:
    arr.append([current_pair,current_count])
pass_count = threshold * no_of_baskets
arr.sort(key=sortsecond,reverse=True)
if len(arr) >=max_print:
    del arr[max_print:]
for i in range(len(arr)):
    if arr[i][1] >= pass_count:
	print '%s\t%d' % (arr[i][0],arr[i][1])
