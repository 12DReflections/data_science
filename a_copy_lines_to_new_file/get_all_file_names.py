#!/usr/bin/python
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

print curr_directory
print file_list