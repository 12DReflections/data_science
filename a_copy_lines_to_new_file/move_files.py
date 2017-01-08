
#!/usr/bin/python
from itertools import islice

import os

path = "input"

# Check current working directory.
curr_directory = os.getcwd()
#print "Current working directory %s" % curr_directory

# Now change the directory
os.chdir( path )
# Check current working directory.
# curr_directory = os.getcwd()
# print "Directory changed successfully %s" % curr_directory

file_list = [f for f in os.listdir('.') if os.path.isfile(f)]
os.chdir( '..' )
# Check current working directory.
curr_directory = os.getcwd()

#print curr_directory
#print file_list


N = 5 # number of lines
for file_name in file_list:
	with open("input/" + file_name, 'r') as myfile:
	    head = [next(myfile) for x in xrange(N)]
	#print head

	with open("output/" + file_name, 'w+') as outfile:
		for item in head:
		  outfile.write("%s" % item)