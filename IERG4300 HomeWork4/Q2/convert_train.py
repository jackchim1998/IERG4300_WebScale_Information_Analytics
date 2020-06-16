import os 
import numpy as np

try:
    os.remove('./data/train_images_eigenspace')
except:
    print "no such file remove"
eigenvector=[]
with open('./data/train_images_eigenvector','r') as f_input:
    for line in f_input:
	line = line.strip()
	pt = line.split()
	for i in range(len(pt)):
	    try:
		pt[i] = float(pt[i])
	    except ValueError:
		print "Error: cannot convert to float"
	eigenvector.append(pt)
eigenvector_np = np.array(eigenvector)#25*784
eigenvector_np_t = eigenvector_np.transpose()#784*25
with open('./data/train_images_center','r') as f_input:
    with open('./data/train_images_eigenspace','w') as f_output:
	for line in f_input:
	    line = line.strip()
	    pt = line.split()
	    for i in range(len(pt)):
		try:
		    pt[i] = float(pt[i])
		except ValueError:
		    print "Error: cannot convert to float"
	    pt_np = np.array(pt)#1*784
	    pt_converted_np = np.dot(pt_np,eigenvector_np_t)#1*25
	    #print(pt_converted_np)
	    for i in range(pt_converted_np.shape[0]):
		f_output.write(str(pt_converted_np[i])+" ")
	    f_output.write("\n")

try:
    os.remove('./data/test_images_eigenspace')
except:
    print "no such file remove"

with open('./data/test_images_center','r') as f_input:
    with open('./data/test_images_eigenspace','w') as f_output:
        for line in f_input:
            line = line.strip()
            pt = line.split()
            for i in range(len(pt)):
                try:
                    pt[i] = float(pt[i])
                except ValueError:
                    print "Error: cannot convert to float"
            pt_np = np.array(pt)#1*784
            pt_converted_np = np.dot(pt_np,eigenvector_np_t)#1*25
            #print(pt_converted_np)
            for i in range(pt_converted_np.shape[0]):
                f_output.write(str(pt_converted_np[i])+" ")
            f_output.write("\n")

for i in range(3):
    with open('./a/init_rand_seed_center'+str(i),'r') as f_input:
	with open('./a/init_rand_seed_converted'+str(i),'w') as f_output:
	    for line in f_input:
		line = line.strip()
		pt = line.split()
		for i in range(len(pt)):
		    try:
		        pt[i] = float(pt[i])
		    except ValueError:
	    	        print "Error: cannot convert to float"
		pt_np = np.array(pt)#1*784
		pt_converted_np = np.dot(pt_np,eigenvector_np_t)#1*25
		#print(pt_converted_np)
		for i in range(pt_converted_np.shape[0]):
		    f_output.write(str(pt_converted_np[i])+" ")
		f_output.write("\n")


