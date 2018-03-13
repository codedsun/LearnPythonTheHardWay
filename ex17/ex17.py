#Prohgram to copy file from one to another
from sys import argv
from os.path import exists

script, filefrom, fileto= argv

print("Copying file form %s to %s"%(filefrom,fileto))
inputfile = open(filefrom).read()


print("The input file is %d bytes long ",len(inputfile))
print("Does the output file exist? %s"%(exists(fileto)))
print("Ready hit run or ctrl+C to abort")
input()
outputfile= open(fileto,'w')
outputfile.write(inputfile)

print("Allright we are done")
outputfile.close()

