#!/usr/bin/env Python



import os

blkpath='/home/smd/lebras/GA/INFRA_ONLY/BLK_STR'
for path, subdirs, files in os.walk(blkpath):
   for filename in files:
     	f = os.path.join(path, filename)
     	print(filename)
     
     	fwd = open(blkpath+'/'+filename, "r")
	
	line = fwd.readline()
	line=line.replace("/n","")
	while '  ' in line:
		line=line.replace("  "," ")	
	print(line)
	values = line.split(" ")
	sta=values[0].replace('\n','')
	rwd = open('/home/smd/lebras/GA/INFRA_ONLY/BLK_INF/'+'BLK.'+sta+'.99999999999.I', "w")
	rwd.write(sta)
	rwd.write(" I 99999999999\n")
        line = fwd.readline()
	rwd.write('#\n')
	while True:
		line = fwd.readline()
		line=line.replace("/n","")
		if not line:
			break
#
# Get rid of all double white space in the string
#
		while '  ' in line:
			line=line.replace("  "," ")
		
		print(line)

		values = line.split(" ")
		rwd.write(values[2].replace('\n',''))
		rwd.write(" 1  0. ")
		rwd.write(values[1])
		rwd.write('\n')
