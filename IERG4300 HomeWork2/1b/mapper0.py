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
threshold=0.005
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
freq_dic={}
current_code=0
for key, value in dic.items():
    if value>=pass_count:
	freq_dic[key]=current_code
	current_code+=1
pair_matrix=[]
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
code_list = [None] * (current_code)
for key, value in freq_dic.items():
    code_list[value]=key

for i in range(current_code):
    for j in range(i,current_code):
	pair_count=None
	if i==j:
	    pair_count = pair_matrix[i][j]
	else:
	    pair_count = pair_matrix[i][j]+pair_matrix[j][i]
	if pair_count >= pass_count:
	    if code_list[i] < code_list[j]:
		print '%s %s\t.' % (code_list[i],code_list[j])
	    else:
		print '%s %s\t.' % (code_list[j],code_list[i])

