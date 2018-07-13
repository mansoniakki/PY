from sys import argv

script, filename = argv
txt = open(filename)

print("Here is your file %s" % filename)

print(txt.read())

txt.close()

filename=input("Type Filename again")
txt=open(filename)
print(txt.read())
txt.close()