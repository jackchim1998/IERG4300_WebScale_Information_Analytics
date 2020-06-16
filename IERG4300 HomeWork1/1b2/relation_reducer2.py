#!/usr/bin/env python

from operator import itemgetter
import sys
import json

k=3
similar_array=[]
userid2=None
current_userid2=None
current_userid1=None
userid1=None
def sortsecond(val):
    return val[1]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    userid1, contentstring = line.split('\t', 1)
    array = contentstring.split(' ')
    # convert to int or double
    try:
	userid1 = int(userid1)
	userid2 = int(array[0])
	similar = float(array[1])
    except ValueError:
	continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_userid1 == userid1:
        similar_array.append([userid2,similar])
	if len(similar_array)>100:
	    similar_array.sort(key=sortsecond,reverse=True)
	    del similar_array[k:]
    else:
        if current_userid1:
	    #print out
            similar_array.sort(key=sortsecond,reverse=True)
            del similar_array[k:]
	    i=0
	    line_print=str(current_userid1)+'\t'
	    while i<k:
		line_print+=' <'+str(similar_array[i][0])+','+str(similar_array[i][1])+'>'
		i+=1
	    print(line_print)
	similar_array=[]
        current_userid1 = userid1
	current_userid2 = userid2
	similar_array.append([userid2,similar])

# do not forget to output the last word if needed!
if current_userid1 == userid1:
    if current_userid1:
        #print out
        similar_array.sort(key=sortsecond,reverse=True)
        del similar_array[k:]
        i=0
        line_print=str(current_userid1)+'\t'
        while i<k:
           line_print+=' <'+str(similar_array[i][0])+','+str(similar_array[i][1])+'>'
           i+=1
	print(line_print)
	
