#!/usr/bin/env python

import sys


current_key=None
count=0
new_centroid=[]
for i in range(25):
    new_centroid.append(0.0)
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    key, content = line.split('\t', 1)
    pt = content.split()
    #error check
    if len(pt) != len(new_centroid):
	print("Error: dimension false for stdin")
        exit
    # sum up
    if current_key is None:
	current_key = key
    if current_key == key:
        for i in range(len(pt)):
	    try:
	        new_centroid[i] += float(pt[i])
	    except ValueError:
	        print("Error: convert to float failed in stdin")
	        exit
        count+=1
    else:
	#calculate and print
	for i in range(len(new_centroid)):
	    value_dim = new_centroid[i]/count
	    print "%f " % value_dim,
	    # clear
	    new_centroid[i]=0.0
	print ""
	count=0
	#sum up
	for i in range(len(pt)):
            try:
                new_centroid[i] += float(pt[i])
            except ValueError:
                print("Error: convert to float failed in stdin")
                exit
        count+=1
	current_key = key


for i in range(len(new_centroid)):
    value_dim = new_centroid[i]/count
    print "%f " % value_dim,
    

