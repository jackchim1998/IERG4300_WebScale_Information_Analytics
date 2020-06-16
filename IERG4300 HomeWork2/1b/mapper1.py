#!/usr/bin/env python

from operator import itemgetter
import sys
cand_pair = {}
#with open('./local_can_pair_basket2.txt') as fp:
with open('cand_pair','r') as fp:
    for line in fp:
        line = line.strip()
        cand_pair[line] = True



# input comes from STDIN (standard input)
set_of_common = set([])

def process(arr):
    #remove duplicate
    new_arr = list(dict.fromkeys(arr))
    del arr
    result = [a for a in new_arr if a not in set_of_common]
    del new_arr
    return result

pair_s=None
no_of_baskets=0
for line in sys.stdin:
    mylist=[]
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line
    words = line.split(" ")
    words = process(words)
    no_of_baskets+=1
    for i in range(len(words)):
	for j in range(i+1,len(words)):
	    if words[i]<words[j]:
		pair_s = words[i]+" "+words[j]
	    else:
		pair_s = words[j]+" "+words[i]
	    if pair_s in cand_pair:
		print '%s\t1' % (pair_s)

    

