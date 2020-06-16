import os

try:
    os.remove('./data/train_images_center')
except:
    print "no such file remove"
image_size=28*28
center= [0.0]*image_size
count=0
with open('./data/train_images','r') as f_input:
    for line in f_input:
	line = line.strip()
	pt = line.split()
	for i in range(len(pt)):
	    try:
		pt[i] = int(pt[i])
	    except ValueError:
		print "Error: cannot convert to int"
	for i in range(len(center)):
	    center[i] += pt[i]
	count+=1

for i in range(len(center)):
    center[i]= center[i]/count	

with open('./data/train_images','r') as f_input:
    with open('./data/train_images_center','w') as f_output:
	for line in f_input:
	    line = line.strip()
	    pt = line.split()
	    for i in range(len(pt)):
		try:
		    pt[i] = float(pt[i])
		except ValueError:
		    print "Error: cannot convert to float"
	    for i in range(len(pt)):
  	        pt[i] = pt[i] - center[i]
		f_output.write(str(pt[i]) + " ")
	    f_output.write("\n")

try:
    os.remove('./data/test_images_center')
except:
    print "no such file remove"

with open('./data/test_images','r') as f_input:
    with open('./data/test_images_center','w') as f_output:
        for line in f_input:
            line = line.strip()
            pt = line.split()
            for i in range(len(pt)):
                try:
                    pt[i] = float(pt[i])
                except ValueError:
                    print "Error: cannot convert to float"
            for i in range(len(pt)):
                pt[i] = pt[i] - center[i]
                f_output.write(str(pt[i]) + " ")
            f_output.write("\n")

for i in range(3):
    try: 
	os.remove('./a/init_rand_seed_center'+str(i))
    except:
	print "no such file remove"
    with open('./a/init_rand_seed'+str(i),'r') as f_input:
	with open('./a/init_rand_seed_center'+str(i),'w') as f_output:
	    for line in f_input:
		line = line.strip()
		pt = line.split()
		for i in range(len(pt)):
                    try:
                        pt[i] = float(pt[i])
                    except ValueError:
                        print "Error: cannot convert to float"
		for i in range(len(pt)):
		     pt[i] = pt[i] - center[i]
		     f_output.write(str(pt[i]) + " ")
		f_output.write("\n")

	
	    
    


