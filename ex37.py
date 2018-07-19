print("using different keywords in this excercise")
print("##########################")
print ("Using DEL")
mylist = [100,200,300,400]
print("My List is ", mylist)
del mylist[0]
print("My List is ", mylist)

print("##########################")
print("Using 'as' and 'with'")
with open('trg.txt') as f:
	text=f.read()
	print (text)

print("##########################")

print("Using Assert")
assert (20 > 10),"It is not true"

print ('c:\'\PY\MyFiles')

print ('My house is \a\a\a\a round the corner')

ten_things = "Apple Orange Brush TV House Rose"
print(len(ten_things))
stuff=ten_things.split(' ')
print("Stuff", stuff)
print(len(stuff))

mlist=['scc', 'dsds', 'wwwww', 'ggggg', 'tytt']
print (mlist)
print(len(mlist))
