from sys import argv
script, filename = argv
print (" We are going to erase %r " % filename)
print("Opening the file.. ")
target = open(filename, 'w')

print ("Truncating file %r, Goodbye!" % filename)
target.truncate()
#target.close()

print("Now I am going to ask you three lines:")

line1 = input("Enter First Line")
line2 = input("Enter Second Line")
line3 = input("Enter third line")
final_line= line1 +"\n"+line2+"\n"+line3+"\n"
print("Final LIne: ", final_line)
print(" I am going to write these lines back to file")
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print(" And finally we close it")
target.close()