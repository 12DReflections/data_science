from itertools import islice


N = 5 # number of lines

with open("input/infile.txt", 'r') as myfile:
    head = [next(myfile) for x in xrange(N)]
print head

with open("output/outfile.txt", 'w+') as outfile:
	for item in head:
	  outfile.write("%s" % item)