#!/usr/bin/env python

from operator import itemgetter
import sys
user_cnt = {}
#with open('./small_indi_cnt_out/part-00000') as fp:
with open('file_sum','r') as fp:
    cnt=0
    for line in fp:
	userid, cnt_str = line.split('\t', 1)
	try:
            cnt = int(cnt_str)
	    userid = int(userid)
        except ValueError:
            continue
	user_cnt[userid] = cnt
	

current_pair = None
pair = None
current_count_rat = 0
current_count=0
current_userid=[0,0]
count = None
similar=0.0
def sortSecond(val):
    return val[1]
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # parse the input we got from mapper.py
    pair, count_str = line.split('\t', 1)
    count=count_str.split(' ')
    userid=pair.split(',')
    
    # convert to int or double
    try:
	count[0] = int(count[0])
	count[1] = int(count[1])
	userid[0] = int(userid[0])
	userid[1] = int(userid[1])
    except ValueError:
	continue
    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_pair == pair:
        current_count_rat += count[0]
	current_count += count[1]
    else:
        if current_pair:
	    #store in counter
            similar = float(current_count_rat)/(user_cnt[current_userid[0]]+user_cnt[current_userid[1]]-current_count)
	    #print '%s\t%f %d %d %d' % (pair,similar,user_cnt[userid[0]],user_cnt[userid[1]],current_count)
	    print '%s\t%f' % (current_pair,similar)
	    
	current_pair = pair
        current_count = count[1]
	current_count_rat = count[0]
	current_userid[0] = userid[0]
	current_userid[1] = userid[1]
        

# do not forget to output the last word if needed!
if current_pair:
    #store in count
    similar = float(current_count_rat)/(user_cnt[current_userid[0]]+user_cnt[current_userid[1]]-current_count)
    print '%s\t%f' % (current_pair,similar)


	
