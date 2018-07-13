from sys import argv
from os.path import exists
script, fromfile, tofile = argv  
print("Copying file from %s to %s " % (fromfile, tofile))

infile = open(fromfile)
indata = infile.read()

print("The input file is %d byte "  % len(indata))

print("Does the aoutput file exist? %r " % exists(tofile))
print("Ready, hit Return to continue, CTRL - C to abort.")
input()

out_file = open(tofile, 'a')
out_file.write("\n")
out_file.write(indata)

print("Alright, Done")

infile.close()
out_file.close()
 