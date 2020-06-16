#!/usr/bin/env python

import sys
import math

centroids=[]
#with open('./tmp_data/tmp_cent_0_0','r') as fp:
#with open('./init_rand_seed1','r') as fp:
with open('f_cent','r') as fp:
    for line in fp:
	line = line.strip()
	cent = line.split()
	for i in range(len(cent)):
	    try:
		cent[i] = float(cent[i])
	    except ValueError:
		print 'ERROR: cannot convert to float in f_cent'
		sys.exit()
	centroids.append(cent)

for line in sys.stdin:
    line = line.strip()
    pt = line.split()
    #convert to int
    for i in range(len(pt)):
        try:
            pt[i] = int(pt[i])
        except ValueError:
            print 'ERROR: cannot convert to int in f_cent'
            sys.exit()
    distance_centroid=None
    current_centriod=None
    index=0
    for cent in centroids:
	tmp_dist=0.0
	if len(pt) != len(cent):
	    print 'ERROR: dimension different between pt and cent'
	    sys.exit()
	for i in range(len(pt)):
	    tmp_dist += (pt[i]-cent[i])*(pt[i]-cent[i])
	if distance_centroid is None:
	    distance_centroid = tmp_dist
	    current_centriod = index
	else:
	    if tmp_dist < distance_centroid :
		distance_centroid = tmp_dist
		current_centriod = index
	index+=1
    print '%d\t%s' % (current_centriod,line)
	
