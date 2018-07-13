from sys import argv

def print_two(arg1, arg2):
	#arg1, arg2 = argv
	print("arg1: %r, arg2: %r " % (arg1, arg2))

def calc_two_no(no1,no2):
	print("sum of %d, %d is %d " % (no1, no2, no1+no2))
	
def check_no (no1):
	print(" 20 time of %d is %d" % (no1, 20 * no1))
	
print_two("ABC", "XYZ")
calc_two_no(78, 79)
check_no (25)

 
