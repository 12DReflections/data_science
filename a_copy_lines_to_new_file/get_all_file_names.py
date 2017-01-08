#!/usr/bin/python
import os

path = "input"

# Check current working directory.
retval = os.getcwd()
#print "Current working directory %s" % retval
# Now change the directory
os.chdir( path )
# Check current working directory.
retval = os.getcwd()
#print "Directory changed successfully %s" % retval

files = [f for f in os.listdir('./input') if os.path.isfile(f)]
print files_list

os.chdir( '..' )
# Check current working directory.
retval = os.getcwd()

print retval
print files_list