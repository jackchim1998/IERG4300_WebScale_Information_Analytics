import math
import os
class centroid:
    pt = None
    count = 0
    final_label = None
    labels = None
    def __repr__(self):
	return str(self.pt) + "\n"
	

total_number_of_rand = 3
centroids=[]
for rand_index in range(total_number_of_rand):
    print "handling %d" % rand_index
    with open("final_output"+str(rand_index),"r") as f_cent:
	for line in f_cent:
	    line = line.strip()
	    pt = line.split()
	    not_pt=False
	    for i in range(len(pt)):
		try:
		    pt[i] = float(pt[i])
		except ValueError:
		    not_pt=True
		    break
	    if not not_pt and len(pt)!=0:
		cent = centroid()
		cent.labels = [0] *10
		cent.pt = list(pt)
	        centroids.append(cent)
    with open("../data/train_images","r") as f_image:
	with open("../data/train_labels","r") as f_label:
	    line_read=0
	    for line_image in f_image:
		line_read+=1
		if line_read%3000 == 0:
		    print "process %d lines" % line_read
		line_label = f_label.readline()
		label=None
		try:
		    label = int(line_label)
		except ValueError:
		    print "cannot convert label to int"
	    	    exit()
		line_image = line_image.strip()
		pt = line_image.split()
		for i in range(len(pt)):
		    try:
			pt[i] = int(pt[i])
		    except ValueError:
			print "cannot convert label to int"
                    	exit()
		#cal diff
		min_diff = float("inf")
		min_diff_cent = -1
		for cent_index in range(len(centroids)):
		    diff = 0.0
		    for i in range(len(pt)):
			diff+= (pt[i] - centroids[cent_index].pt[i]) ** 2
		    diff = math.sqrt(diff)
		    if diff < min_diff:
			min_diff_cent = cent_index
			min_diff = diff

		centroids[min_diff_cent].labels[label] +=1
		centroids[min_diff_cent].count +=1
    try:
	os.remove("verify"+str(rand_index))
    except:
	print "no such file to remove"
    with open("verify"+str(rand_index),"w") as f_out:
	for cent_index in range(len(centroids)):
	    tmp_label_count = -1
	    for i in range(len(centroids[cent_index].labels)):
    	        if centroids[cent_index].labels[i] > tmp_label_count:
		    tmp_label_count = centroids[cent_index].labels[i]
		    centroids[cent_index].final_label = i
	    label_count = centroids[cent_index].labels[centroids[cent_index].final_label]
	    f_out.write("centroid "+str(cent_index)+": label "+str(centroids[cent_index].final_label)+", count "+str(label_count)+", accuracy "+str(float(label_count)/centroids[cent_index].count)+"\n")
    centroids=[]
