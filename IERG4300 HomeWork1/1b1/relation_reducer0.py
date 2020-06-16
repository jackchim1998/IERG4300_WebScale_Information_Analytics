#!/usr/bin/env python

from operator import itemgetter
import sys
import json

current_movieid = None
movieid = None
same_movie_array=[]
userid = None
rating = None
cuid_last2_digit = 82 #1155094482
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    movieid, contentstring = line.split('\t', 1)
    array = contentstring.split(' ')
    # convert to int or double
    try:
	userid = int(array[0])
	rating = float(array[1])
    except ValueError:
	continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_movieid == movieid:
        same_movie_array.append([userid,rating])
    else:
        if current_movieid:
	    #print out
            for i in range(len(same_movie_array)):
		j=i+1
		while j<len(same_movie_array):
		    if same_movie_array[i][0]%100 == cuid_last2_digit or same_movie_array[j][0]%100 == cuid_last2_digit:
   	 		if same_movie_array[i][1] == same_movie_array[j][1]:
   			    if same_movie_array[i][0] < same_movie_array[j][0]:
			        print '%s,%s\t%d %d' % (same_movie_array[i][0],same_movie_array[j][0],1,1)
    			    else:
                                print '%s,%s\t%d %d' % (same_movie_array[j][0],same_movie_array[i][0],1,1)
		        else:
			    if same_movie_array[i][0] < same_movie_array[j][0]:
                                print '%s,%s\t%d %d' % (same_movie_array[i][0],same_movie_array[j][0],0,1)
                            else:
                                print '%s,%s\t%d %d' % (same_movie_array[j][0],same_movie_array[i][0],0,1)
		    j+=1
	same_movie_array=[]
        current_movieid = movieid
	same_movie_array.append([userid,rating])

# do not forget to output the last word if needed!
if current_movieid == movieid:
    if current_movieid:
        for i in range(len(same_movie_array)):
            j=i+1
            while j<len(same_movie_array):
		if same_movie_array[i][0]%100 == cuid_last2_digit or same_movie_array[j][0]%100 == cuid_last2_digit:
                    if same_movie_array[i][1] == same_movie_array[j][1]:
                        if same_movie_array[i][0] < same_movie_array[j][0]:
                            print '%s,%s\t%d %d' % (same_movie_array[i][0],same_movie_array[j][0],1,1)
                        else:
                            print '%s,%s\t%d %d' % (same_movie_array[j][0],same_movie_array[i][0],1,1)
                    else:
                        if same_movie_array[i][0] < same_movie_array[j][0]:
                            print '%s,%s\t%d %d' % (same_movie_array[i][0],same_movie_array[j][0],0,1)
                        else:
                            print '%s,%s\t%d %d' % (same_movie_array[j][0],same_movie_array[i][0],0,1)

		j+=1
	
