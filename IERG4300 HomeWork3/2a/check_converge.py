import math
number_of_loop = 51
rand_seed=0
old_data=[]
new_data=[]
result=[]
for rand_seed in range(3):
	for i in range(number_of_loop):
	    file_name = "./tmp_data/tmp_cent_"+str(rand_seed)+"_"+str(i)
	    if i==0:
		with open(file_name,"r") as f:
		    for line in f:
			line = line.strip()
			pt = line.split()
			for j in range(len(pt)):
			    try:
				pt[j] = float(pt[j])
			    except ValueError:
				print "ERROR: converge to float failed"
			old_data.append(pt)
	    else:
		with open(file_name,"r") as f:
		    for line in f:
			line = line.strip()
			pt = line.split()
			for j in range(len(pt)):
			    try:
				pt[j] = float(pt[j])
			    except ValueError:
				print "ERROR: converge to float failed"
			new_data.append(pt)
		for j in range(len(new_data)):
		    tmp_mini_diff = float("inf")
		    for k in range(len(old_data)):
			tmp_diff=0.0
			for dim in range(len(old_data[0])):
			    tmp_diff += (new_data[j][dim] - old_data[k][dim]) ** 2
			tmp_diff=math.sqrt(tmp_diff)
			if tmp_diff < tmp_mini_diff:
			    tmp_mini_diff = tmp_diff
		    result.append(tmp_mini_diff)
		result.sort(reverse = True)
		print "%d -> %d" % (i-1,i),
		print(result)
		result=[]
		old_data=[]
		old_data = list(new_data)
		new_data=[]
		
