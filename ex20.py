from sys import argv

#Assigning arguments to variables
script, input_file = argv

#Function to read the file
def print_all(f):
	print(f.read())

#function to rewind the file
def rewind(f):
	f.seek(0)

#function to print 1 line
def print_one_line(line_count, f):
	print("Line Number: %d Line: %s " % (line_count, f.readline()))
#Open the file
current_file = open(input_file)
#Print All File
print_all(current_file)

#Rewind the file
rewind(current_file)

current_line = 1
print_one_line(current_line, current_file)
current_line = 2
print_one_line(current_line, current_file)
#Close the files
current_file.close()