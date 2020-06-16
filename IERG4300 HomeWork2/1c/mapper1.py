#!/usr/bin/env python

from operator import itemgetter
import sys
cand_tri = {}
#with open('./cand_pair') as fp:
with open('cand_tri','r') as fp:
    cnt=0
    for line in fp:
        line = line.strip()
        cand_tri[line] = True



# input comes from STDIN (standard input)
set_of_common = set([])

def process(arr):
    #remove duplicate
    new_arr = list(dict.fromkeys(arr))
    del arr
    result = [a for a in new_arr if a not in set_of_common]
    del new_arr
    return result

tri_s=None
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line
    words = line.split(" ")
    words = process(words)
    for i in range(len(words)):
	for j in range(i+1,len(words)):
	    for k in range(j+1,len(words)):
	        tmp_arr=[]
		tmp_arr.append(words[i])
                tmp_arr.append(words[j])
                tmp_arr.append(words[k])
		tmp_arr.sort()
		tri_s = tmp_arr[0] + " " +tmp_arr[1] + " " +tmp_arr[2]
	    	if tri_s in cand_tri:
		    print '%s\t1' % (tri_s)

    

