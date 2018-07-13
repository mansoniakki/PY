def ret_my_sal (name):
	if name=='Kamal':
		return 20000
	elif name == 'Mangal':
		return 30000
	else:
		return 0

mysal=ret_my_sal('Mangal')
print ("My Salary is: ", mysal)