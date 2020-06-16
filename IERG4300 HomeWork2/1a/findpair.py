#!/usr/bin/env python

import sys
import time
class pair:
    x=0
    y=0
    count=0
    def __str__(self):
        return "pair: "+str(self.x)+", "+str(self.y)+" count: "+str(self.count)
    def __repr__(self):
        return "pair: "+str(self.x)+", "+str(self.y)+" count: "+str(self.count)+"\n"

set_of_common = set([])
def process(arr):
    #remove duplicate
    new_arr = list(dict.fromkeys(arr))
    del arr
    #filter common words
    result = [a for a in new_arr if a not in set_of_common]
    del new_arr
    return result

def sort_count(e):
    return e.count

threshold=0.005
no_baskets=0
dic = {}
f = open("shakespeare_basket1","r")
number_of_line=float("inf")
#number_of_line=2000
number_print=40
lineread=0
start =time.time()
# input comes from STDIN (standard input)
for line in f:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    words = process(words)
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word in dic:
            dic[word]+=1
        else:
            dic[word]=1
    no_baskets+=1
    lineread+=1
    if lineread>=number_of_line:
        break

dic_freq={}
pass_count = no_baskets*threshold
current_code=0
for key, value in dic.items():
    if value>=pass_count:
        dic_freq[key]=current_code
        current_code+=1

end = time.time()
print("frequent items complete. total: "+ str(current_code))
print("number of baskets: %d, threshold: %f, pass_count: %f" % (no_baskets,threshold,pass_count))
print(end-start)
#del dic
f.seek(0)
lineread=0
pair_matrix=[]
for i in range(current_code):
    rowList=[]
    for j in range(current_code):
        rowList.append(0)
    pair_matrix.append(rowList)
for line in f:
    line = line.strip()
    words = line.split()
    words = process(words)
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if words[i] in dic_freq and words[j] in dic_freq:
                code_x = dic_freq[words[i]]
                code_y = dic_freq[words[j]]
                #check pair exist
                pair_matrix[code_x][code_y]+=1
                    
    lineread+=1
    if lineread>=number_of_line:
        break

#filter, sort and print
code_list = [None] * (current_code)
for key,value in dic_freq.items():
    code_list[value]=key
pair_arr_freq=[]
for i in range(current_code):
    for j in range(i,current_code):
        new_pair = pair()
        new_pair.x=i
        new_pair.y=j
        if i==j:
            new_pair.count = pair_matrix[i][j]
        else:
            new_pair.count = pair_matrix[i][j] + pair_matrix[j][i]
        pair_arr_freq.append(new_pair)
pair_arr_freq.sort(key=sort_count,reverse=True)
index_not_pass=None
for i in range(len(pair_arr_freq)):
    if pair_arr_freq[i].count < pass_count:
        index_not_pass = i
if index_not_pass != None:
    del pair_arr_freq[index_not_pass:]
print("threshold is %f, pass_count is %f" % (threshold,pass_count))
for i in range(min(number_print,len(pair_arr_freq))):
    print("pair: \"%s %s\" count: %d" % (code_list[pair_arr_freq[i].x], code_list[pair_arr_freq[i].y], pair_arr_freq[i].count)) 
end = time.time()
print(end-start)

