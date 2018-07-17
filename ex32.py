print("working with list")
the_count = [1,2,3,4,5,6]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
for i in the_count:
	print("This is count %d " % i)

for i in fruits:
	print("This is %s " % i)

for i in change:
	print("I got %r " % i)
	
print ("\n\nNow creating an empty list")

element=[]

for i in range (0,6):
	print("Added %d to the list " %i)
	element.append(i)

for i in element:
	print("Element was %d " % i)


