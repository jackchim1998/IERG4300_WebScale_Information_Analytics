#!/usr/bin/env python

from operator import itemgetter
import sys

current_userid = None
current_count = 0
userid = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    userid, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if current_userid == None:
        current_userid = userid
        current_count += count
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_userid == userid:
        current_count += count
    else:
        if current_userid:
            # write result to STDOUT
            print '%s\t%s' % (current_userid, current_count)
        current_count = count
        current_userid = userid

# do not forget to output the last word if needed!
if current_userid == userid:
    print '%s\t%s' % (current_userid, current_count)
