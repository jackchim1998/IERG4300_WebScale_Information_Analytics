#!/usr/bin/env python

import sys

# input comes from STDIN (standard input)
set_of_common = set([])

def process(arr):
    #remove duplicate
    new_arr = list(dict.fromkeys(arr))
    del arr
    result = [a for a in new_arr if a not in set_of_common]
    del new_arr
    return result

dic = {}
_raw_input=[]
no_of_baskets=0
threshold=0.0025
for line in sys.stdin:
    mylist=[]
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line
    words = line.split(" ")
    words = process(words)
    for word in words:
	if word in dic:
	    dic[word]+=1
	else:
	    dic[word]=1
    no_of_baskets+=1
    _raw_input.append(words)
    
pass_count = no_of_baskets*threshold
freq_dic={}#frequent items dictionary version
current_code=0 # also the length pf frequent items
for key, value in dic.items():
    if value>=pass_count:
	freq_dic[key]=current_code
	current_code+=1
del dic
pair_matrix=[]#using to count pair
for i in range(current_code):
    rowList=[]
    for j in range(current_code):
        rowList.append(0)
    pair_matrix.append(rowList)
for words in _raw_input:
    for i in range(len(words)):
	for j in range(i+1,len(words)):
	    if words[i] in freq_dic and words[j] in freq_dic:
		code_x = freq_dic[words[i]]
		code_y = freq_dic[words[j]]
		pair_matrix[code_x][code_y]+=1
code_list = [None] * (current_code)#frequent items array version
for key, value in freq_dic.items():
    code_list[value]=key
freq_pair_dic={}#freq pairs in code
for i in range(current_code):
    for j in range(i+1,current_code):
	pair_count = pair_matrix[i][j]+pair_matrix[j][i]
	if pair_count >= pass_count:
	    if code_list[i] < code_list[j]:
		freq_pair_dic[code_list[i]+" "+code_list[j]]=True
	    else:
		freq_pair_dic[code_list[j]+" "+code_list[i]]=True
#generate candidate triplets dictionary, key is number with space, value is count
cand_tri_dic={}
for words in _raw_input:
    for i in range(len(words)):
        for j in range(i+1,len(words)):
	    for k in range(j+1,len(words)):
		if words[i] in freq_dic and words[j] in freq_dic and words[k] in freq_dic:
		    tmp_arr=[]
		    tmp_arr.append(words[i])
		    tmp_arr.append(words[k])
		    tmp_arr.append(words[j])
		    tmp_arr.sort()
		    if (tmp_arr[0]+" "+tmp_arr[1]) in freq_pair_dic or (tmp_arr[0]+" "+tmp_arr[2]) in freq_pair_dic or (tmp_arr[1]+" "+tmp_arr[2])  in freq_pair_dic:
		    	s = str(tmp_arr[0])+" "+str(tmp_arr[1])+" "+str(tmp_arr[2])
		    	if s in cand_tri_dic:
			    cand_tri_dic[s]+=1
			else:
			    cand_tri_dic[s]=1

for key,value in cand_tri_dic.items():
    if value > pass_count:
	print '%s\t.' % (key)

